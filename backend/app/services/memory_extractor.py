from app.core.openai_client import OpenAIClient
from app.core.schemas import MemoryExtractionResult
import textwrap

class MemoryExtractor:

    def __init__(self):
        self.client = OpenAIClient()

    async def extract(self, messages: list[str]) -> MemoryExtractionResult:
        """
        Extracts user preferences, emotional patterns,
        and long-term factual memories from chat messages.
        """

        combined_text = "\n".join(messages)

        prompt = textwrap.dedent(f"""
        You will receive a list of chat messages from a user.

        Your job is to EXTRACT three specific types of long-term memory:

        1. User Preferences
           - likes, dislikes, habits, interests, conversational style, etc.

        2. Emotional Patterns
           - recurring emotions, tendencies (e.g., anxious, optimistic, sarcastic)

        3. Factual Memories
           - stable personal data like location, family, job, birthday, goals

        IMPORTANT RULES:
        - Only extract memories that are STABLE and LONG-TERM.
        - Ignore temporary feelings or one-time events.
        - Output STRICT JSON ONLY.

        Now extract memories from the following messages:
        \"\"\"
        {combined_text}
        \"\"\"

        Return JSON in EXACT format:
        {{
            "user_preferences": [
                {{"topic": "...", "preference": "..."}}
            ],
            "emotional_patterns": [
                {{"pattern": "..."}}
            ],
            "factual_memories": [
                {{"fact": "..."}}
            ]
        }}
        """)

        # Call LLM in JSON mode
        result_text = await self.client.generate(prompt, json_mode=True)

        # Validate structured output using Pydantic
        validated = MemoryExtractionResult.model_validate_json(result_text)

        return validated