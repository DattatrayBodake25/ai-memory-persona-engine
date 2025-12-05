# AI Memory & Persona Engine System

This project is a full-stack AI-powered system that demonstrates long-term memory extraction from conversational messages and dynamic persona-based response generation. It integrates a structured backend service built with FastAPI and a modern interactive frontend built with React and TailwindCSS. The system is designed to process user messages, infer long-term behavioral and factual patterns, and respond in different conversational styles while maintaining consistency with extracted memory.

The application includes a memory extraction pipeline, a persona transformation engine, and a polished UI for interaction — allowing users to send a message, view both neutral and persona-styled responses side-by-side, and visualize extracted memories in collapsible sections.

## Features
### Memory Extraction
- Identifies user preferences
- Detects emotional patterns
- Extracts factual details
- Stores results in a structured SQLite database
- Ensures consistent structured output via OpenAI’s JSON response format

### Persona-Based AI Responses
Generates:
- Neutral response
- Persona-styled rewritten response

Supported persona styles:
- Calm Mentor
- Witty Friend
- Therapist
- Strict Coach
- Playful Buddy

### Modern Frontend UI
- Collapsible memory viewer
- Persona style selector
- Side-by-side AI responses
- Auto-clearing input box
- Toast notifications
- Smooth loading animations
- Clean minimalistic layout built with TailwindCSS

## Folder Structure
```bash
gupshupp-assignment/
│
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── routes_memory.py
│   │   │   ├── routes_personality.py
│   │   │   └── routes_test.py
│   │   │
│   │   ├── core/
│   │   │   ├── config.py
│   │   │   ├── openai_client.py
│   │   │   └── schemas.py
│   │   │
│   │   ├── services/
│   │   │   ├── memory_extractor.py
│   │   │   ├── personality_engine.py
│   │   │   └── storage.py
│   │   │
│   │   ├── db/
│   │   │   ├── memory.db
│   │   │   └── models.py
│   │   │
│   │   ├── main.py
│   │   └── __init__.py
│   │
│   ├── requirements.txt
│   └── README.md
│
├── frontend/
│   ├── src/
│   │   ├── components/
│   │   │   ├── MemoryView.jsx
│   │   │   ├── ChatInput.jsx
│   │   │   ├── PersonalitySelector.jsx
│   │   │   ├── ResponsePreview.jsx
│   │   │   ├── ChatBubble.jsx
│   │   │   ├── LoaderSpinner.jsx
│   │   │   ├── TypingIndicator.jsx
│   │   │   └── Toast.jsx
│   │   │
│   │   ├── services/
│   │   │   ├── api.js
│   │   │   └── config.js
│   │   │
│   │   └── App.jsx
│   │
│   ├── public/
│   ├── package.json
│   └── README.md
│
└── README.md
```

## Backend Architecture
Memory Extraction Module
- Processes up to 30 conversational messages
- Uses OpenAI (gpt-mini-4o) with strict JSON schema enforcement
- Extracts:
  - Preferences
  - Emotional patterns
  - Factual memories
- Results are stored in SQLite for retrieval and persistent personalization.

Personality Engine
- Generates a neutral response based on the user’s message
- Rewrites the response into a chosen persona style
- Maintains clarity and consistency across tone transformations

OpenAI Wrapper
A unified client ensures all requests:
- Use the selected model
- Support optional JSON-mode generation
- Return clean text outputs

## API Endpoints
1. Extract Memory
```bash
POST /memory/extract
```
Request
```bash
{
  "messages": ["message1", "message2", "..."]
}
```
Response
```
{
  "user_preferences": [...],
  "emotional_patterns": [...],
  "factual_memories": [...]
}
```

2. Get All Stored Memory
```bash
GET /memory/all
```

3. Transform Message with Persona
```bash
POST /persona/transform
```

Request
```
{
  "message": "Hello",
  "persona": "witty friend"
}
```
Response
```
{
  "neutral_response": "...",
  "styled_response": "..."
}
```

4. Health Check
```bash
GET /ping
```

## Frontend Architecture
Highlights:
- Built with React + Vite
- TailwindCSS for styling
- Reusable UI components
- Clean message input system
- Side-by-side AI Responses panel
- Memory viewer with collapsible sections
- Toast notifications for warnings/errors
- Instant UI feedback with loading indicators

The user flow:
- Memory loads automatically on startup
- User selects a persona
- User enters a message
- UI displays:
  - The typed message
  - Both neutral and persona-styled responses

## Installation & Running Locally
Backend
```bash
cd backend

python -m venv venv

venv\Scripts\activate        # Windows

pip install -r requirements.txt

uvicorn app.main:app --reload --port 8000
```

Backend runs at:
```bash
http://localhost:8000
```

Swagger Docs:
```bash
http://localhost:8000/docs
```

Frontend
```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:
```bash
http://localhost:5173/
```

## Project Overview (Descriptive Summary)

This system demonstrates an end-to-end workflow for building memory-aware AI conversation tools. The backend uses structured prompt engineering and schema-based extraction to identify long-term user traits from chat history, such as preferences, emotional tendencies, and factual details. These memories are stored persistently and can influence future interactions.

On top of this, the application integrates a persona engine capable of rewriting responses into various conversational tones while preserving meaning. The frontend provides a clean, intuitive interface that displays extracted memory, enables persona selection, and shows both neutral and styled AI responses side-by-side for comparison. Together, these components create a highly interactive and extensible AI companion experience, suitable for personalization use cases, behavioral modeling, and conversational agents.

## Tech Stack Summary
Backend
- FastAPI
- Python 3.11.9
- OpenAI (gpt-mini-4o)
- SQLite + SQLAlchemy
- Pydantic
- Uvicorn

Frontend
- React 18
- Vite
- TailwindCSS
- Axios
- Lucide Icons

# THANK YOU!
