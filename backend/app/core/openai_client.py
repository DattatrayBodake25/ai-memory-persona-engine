from openai import OpenAI
from .config import OPENAI_API_KEY, OPENAI_MODEL

# Create and reuse a single OpenAI client instance.
# This is more efficient than re-creating the client for every request.
client = OpenAI(api_key=OPENAI_API_KEY)


class OpenAIClient:
    """
    A simple wrapper class around the OpenAI Chat Completions API.
    This keeps API interaction clean and centralized.
    """

    def __init__(self, model: str = OPENAI_MODEL):
        # Store which OpenAI model we want to use (configured in .env)
        self.model = model

    async def generate(self, prompt: str, json_mode: bool = False):
        """
        Sends a prompt to OpenAI and returns the model's response.

        Parameters:
        - prompt (str): The text we want the model to respond to.
        - json_mode (bool): If True, we request a strict JSON output from OpenAI.

        This function supports:
        - Normal natural language responses  
        - Strict JSON-only responses (useful for memory extraction)  
        """

        # OpenAI Chat API requires messages structure
        messages = [
            {"role": "user", "content": prompt}
        ]

        # If strict JSON output is required
        if json_mode:
            response = client.chat.completions.create(
                model=self.model,
                messages=messages,
                response_format={"type": "json_object"}  # Ensures valid JSON output
            )
        else:
            # Standard text-based response
            response = client.chat.completions.create(
                model=self.model,
                messages=messages
            )

        # Extract and return the assistant's message content
        return response.choices[0].message.content