from sqlalchemy.orm import Session
import uuid
import datetime
from app.domain.smart_city_traffic_manager.models import AgenticSmartCityTrafficManagerSession, AgenticSmartCityTrafficManagerItem
from app.domain.smart_city_traffic_manager.schemas import AgenticSmartCityTrafficManagerSessionCreate, AgenticSmartCityTrafficManagerItemCreate

class AgenticSmartCityTrafficManagerService:
    @staticmethod
    def create_session(db: Session, data: AgenticSmartCityTrafficManagerSessionCreate) -> AgenticSmartCityTrafficManagerSession:
        db_obj = AgenticSmartCityTrafficManagerSession(
            id=f"SESS-{uuid.uuid4().hex[:8]}",
            task_prompt=data.task_prompt,
            status="COMPLETED",
            safety_tier="GREEN",
            confidence_score=0.98,
            metadata_json=data.metadata_json or {}
        )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj

    @staticmethod
    def get_session(db: Session, session_id: str) -> AgenticSmartCityTrafficManagerSession:
        return db.query(AgenticSmartCityTrafficManagerSession).filter(AgenticSmartCityTrafficManagerSession.id == session_id).first()
