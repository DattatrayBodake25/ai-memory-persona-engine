from fastapi import APIRouter
from app.services.memory_extractor import MemoryExtractor
from app.services.storage import MemoryStorage
from app.core.schemas import ExtractMemoryRequest, MemoryExtractionResult

# Router for all memory-related endpoints
router = APIRouter()

# Instantiate the memory extraction engine and DB storage helper
memory_extractor = MemoryExtractor()
memory_storage = MemoryStorage()


@router.post("/extract", response_model=MemoryExtractionResult)
async def extract_memory(request: ExtractMemoryRequest):
    """
    Main API endpoint for LONG-TERM MEMORY extraction.

    Workflow:
    1. Accept a list of user messages (raw text inputs)
    2. Pass them to the MemoryExtractor → LLM processes and produces:
        - user preferences
        - emotional patterns
        - factual memories
    3. Validate & structure the extracted output (schema-validated)
    4. Save the result to the database
    5. Return the extracted memory to the client

    This endpoint is usually used only once per session,
    when the system receives ~30 user messages to analyze.
    """

    # Step 1: Run memory extraction logic (LLM-driven)
    result = await memory_extractor.extract(request.messages)

    # Step 2: Persist extracted memory to the database
    memory_storage.save_memory(result)

    # Step 3: Return structured memory back to the client
    return result


@router.get("/all")
async def get_all_memory():
    """
    Returns all stored memory from the database.

    Useful for:
    - Debugging memory module
    - Loading memory into frontend UI on startup
    - Demonstrating persistence for assignment reviewers
    """
    return memory_storage.get_all_memory()