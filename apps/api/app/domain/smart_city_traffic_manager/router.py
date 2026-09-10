from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.domain.smart_city_traffic_manager.schemas import AgenticSmartCityTrafficManagerSessionCreate, AgenticSmartCityTrafficManagerSessionResponse
from app.domain.smart_city_traffic_manager.service import AgenticSmartCityTrafficManagerService

router = APIRouter(prefix="/api/v1/smart_city_traffic_manager", tags=["Agentic Smart City Traffic Manager Domain"])

@router.post("/sessions", response_model=AgenticSmartCityTrafficManagerSessionResponse, status_code=status.HTTP_201_CREATED)
def create_domain_session(data: AgenticSmartCityTrafficManagerSessionCreate, db: Session = Depends(get_db)):
    """
    Creates a new FastAPI domain session for Agentic Smart City Traffic Manager.
    """
    return AgenticSmartCityTrafficManagerService.create_session(db, data)

@router.get("/sessions/{session_id}", response_model=AgenticSmartCityTrafficManagerSessionResponse)
def get_domain_session(session_id: str, db: Session = Depends(get_db)):
    obj = AgenticSmartCityTrafficManagerService.get_session(db, session_id)
    if not obj:
        raise HTTPException(status_code=404, detail="Domain session not found")
    return obj
