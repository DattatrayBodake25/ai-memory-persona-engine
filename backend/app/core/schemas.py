from pydantic import BaseModel
from typing import List


# Memory Extraction Output Models
class PreferenceItem(BaseModel):
    """Represents one extracted user preference."""
    topic: str
    preference: str


class EmotionalPatternItem(BaseModel):
    """Represents one emotional behavior or pattern the user shows."""
    pattern: str


class FactualMemoryItem(BaseModel):
    """Represents a factual detail about the user worth remembering."""
    fact: str


class MemoryExtractionResult(BaseModel):
    """
    Final structured memory extracted from user messages.
    Returned by the /memory/extract endpoint.
    """
    user_preferences: List[PreferenceItem] = []
    emotional_patterns: List[EmotionalPatternItem] = []
    factual_memories: List[FactualMemoryItem] = []


# API Request Models
class ExtractMemoryRequest(BaseModel):
    """Incoming request containing 30 raw chat messages."""
    messages: List[str]



# Persona Transformation Models
class PersonalityRequest(BaseModel):
    """Request for transforming an AI reply into a persona style."""
    message: str
    persona: str


class PersonalityResponse(BaseModel):
    """
    Response containing:
    - a neutral AI reply
    - a rewritten reply in the selected persona
    """
    neutral_response: str
    styled_response: str