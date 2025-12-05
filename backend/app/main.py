from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import routes_memory, routes_personality, routes_test
from app.db.models import init_db

app = FastAPI(title="Gupshupp AI Assignment")

# Initialize DB tables
init_db()

# Allow frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routes
app.include_router(routes_test.router, prefix="/test", tags=["Test"])
app.include_router(routes_memory.router, prefix="/memory", tags=["Memory"])
app.include_router(routes_personality.router, prefix="/persona", tags=["Persona"])


@app.get("/")
def root():
    return {"message": "Gupshupp Assignment Backend Running"}