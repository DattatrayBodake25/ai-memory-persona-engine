from fastapi import APIRouter
from app.core.schemas import PersonalityRequest, PersonalityResponse
from app.services.personality_engine import PersonalityEngine

# Router for persona-based response generation
router = APIRouter()

# Initialize the persona engine (LLM-based rewriting)
persona_engine = PersonalityEngine()


@router.post("/transform", response_model=PersonalityResponse)
async def transform_personality(request: PersonalityRequest):
    """
    Generates TWO responses for the given user message:

    1. Neutral Response
       - A straightforward, unbiased reply from the AI.
       - Ensures the model always provides a grounded, helpful message.

    2. Persona-Styled Response
       - The same message rewritten into the user's selected tone.
       - Supported personas include: calm mentor, witty friend,
         therapist-style, strict coach, playful buddy, etc.

    This endpoint is responsible for showing:
    ✔ before/after transformation  
    ✔ tone shift accuracy  
    ✔ correct persona styling  

    Flow:
    - Accept user message + selected persona style
    - Call the PersonalityEngine → which handles LLM prompting
    - Return structured response to the frontend
    """

    result = await persona_engine.generate_persona_response(
        request.message,
        request.persona
    )

    return result