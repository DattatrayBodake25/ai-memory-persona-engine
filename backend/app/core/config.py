from dotenv import load_dotenv
import os

# Load environment variables from the .env file into the system
load_dotenv()

# Retrieve the OpenAI API key from environment variables.
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Choose which OpenAI model the system should use.
OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-mini-4o")