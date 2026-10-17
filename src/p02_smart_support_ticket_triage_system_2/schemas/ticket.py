from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

Category = Literal[
    "lms and classroom support",
    "student account management",
    "enrolment and deferments",
    "examinations and results",
    "fees and finances",
    "document services",
    "student community",
]
NatureOfCase = Literal["incident", "service request", "inquiry", "complaint"]


class TicketEntry(BaseModel):
    """what a student sends. only two fields are required"""

    # remove spaces at both ends of the email and description, and reject unknown fields
    model_config = ConfigDict(str_strip_whitespace=True, extra="forbid")

    description: str = Field(min_length=10, max_length=5000)


class Ticket(BaseModel):
    """what the llm returns; exactly this shape"""

    subject: str = Field(min_length=1, max_length=255)
    category: Category
    nature_of_case: NatureOfCase
    description: str = Field(min_length=1, max_length=8000)
