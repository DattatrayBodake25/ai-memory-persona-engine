from sqlalchemy.orm import Session
from app.db.models import (
    UserPreference,
    EmotionalPattern,
    FactualMemory,
    SessionLocal
)
from app.core.schemas import MemoryExtractionResult


class MemoryStorage:

    def __init__(self):
        pass

    def save_memory(self, memory: MemoryExtractionResult):
        """
        Saves MemoryExtractionResult into SQLite using SQLAlchemy ORM.
        """

        db: Session = SessionLocal()

        try:
            # Save User Preferences
            for pref in memory.user_preferences:
                db_pref = UserPreference(
                    topic=pref.topic,
                    preference=pref.preference
                )
                db.add(db_pref)

     
            # Save Emotional Patterns
            for emo in memory.emotional_patterns:
                db_emo = EmotionalPattern(pattern=emo.pattern)
                db.add(db_emo)

     
            # Save Factual Memories
            for fact in memory.factual_memories:
                db_fact = FactualMemory(fact=fact.fact)
                db.add(db_fact)

            db.commit()

        except Exception as e:
            db.rollback()
            raise e

        finally:
            db.close()

    def get_all_memory(self):
        """
        Retrieve all stored memory from DB (useful for UI).
        """

        db: Session = SessionLocal()

        prefs = db.query(UserPreference).all()
        emos = db.query(EmotionalPattern).all()
        facts = db.query(FactualMemory).all()

        db.close()

        return {
            "user_preferences": [
                {"topic": p.topic, "preference": p.preference} for p in prefs
            ],
            "emotional_patterns": [
                {"pattern": e.pattern} for e in emos
            ],
            "factual_memories": [
                {"fact": f.fact} for f in facts
            ]
        }