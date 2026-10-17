class LLMError(Exception):
    """parent type for every llm failure"""


class LLMUnavailableError(LLMError):
    """the llm could not be reached: timeout, rate limit, provider down."""


class InvalidLLMResponseError(LLMError):
    """the llm answered, but its answer failed validation"""
