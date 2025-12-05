from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite:///./app/db/memory.db"

Base = declarative_base()

# User Preferences
class UserPreference(Base):
    __tablename__ = "user_preferences"

    id = Column(Integer, primary_key=True, index=True)
    topic = Column(String, nullable=False)
    preference = Column(String, nullable=False)


# Emotional Patterns
class EmotionalPattern(Base):
    __tablename__ = "emotional_patterns"

    id = Column(Integer, primary_key=True, index=True)
    pattern = Column(String, nullable=False)


# Factual Memories
class FactualMemory(Base):
    __tablename__ = "factual_memories"

    id = Column(Integer, primary_key=True, index=True)
    fact = Column(String, nullable=False)


# DB Engine + Session
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    Base.metadata.create_all(bind=engine)