from app.core.openai_client import OpenAIClient
from app.core.schemas import PersonalityResponse
import textwrap

class PersonalityEngine:

    def __init__(self):
        self.client = OpenAIClient()

    async def generate_persona_response(self, message: str, persona: str) -> PersonalityResponse:
        """
        Generates:
        1. A neutral response
        2. A persona-transformed response
        """

        # Step 1: NEUTRAL RESPONSE
        neutral_prompt = textwrap.dedent(f"""
        Respond to the following message in a neutral, helpful assistant tone.

        Message:
        \"{message}\"
        """)

        neutral_response = await self.client.generate(neutral_prompt)


        # Step 2: PERSONA RESPONSE
        persona_prompt = textwrap.dedent(f"""
        Transform the following assistant response into the style of: **{persona}**

        RULES:
        - Preserve the core meaning.
        - Do NOT add unrelated facts.
        - Apply tone, style, personality, and attitude appropriate to the persona.
        - Output plain text only.

        Original Response:
        \"{neutral_response}\"
        """)

        styled_response = await self.client.generate(persona_prompt)

        return PersonalityResponse(
            neutral_response=neutral_response.strip(),
            styled_response=styled_response.strip()
        )