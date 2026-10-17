import logging

from fastapi import APIRouter, HTTPException, status

from ..errors.llm import InvalidLLMResponseError, LLMUnavailableError
from ..schemas.ticket import Ticket, TicketEntry
from ..services.llm import structure_ticket

logger = logging.getLogger(__name__)
router = APIRouter(prefix="/tickets", tags=["Tickets"])


@router.post("/", response_model=Ticket, status_code=status.HTTP_201_CREATED)
async def create_ticket(ticket_data: TicketEntry):
    """create a ticket"""

    try:
        llm_response: Ticket = await structure_ticket(ticket_data.description)

        return llm_response
    except LLMUnavailableError as error:
        logger.exception("llm unavailable")

        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="service unavailable. please try again shortly.",
        ) from error
    except InvalidLLMResponseError as error:
        logger.exception("llm returned invalid output")

        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail="we could not process your ticket. please try again",
        ) from error
