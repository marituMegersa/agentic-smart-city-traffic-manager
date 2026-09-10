from pydantic import BaseModel
from typing import List, Dict, Any, Optional

class AgentState(BaseModel):
    task_id: str
    status: str = "INITIALIZED"
    current_agent: str = "Orchestrator"
    history: List[Dict[str, Any]] = []
    metadata: Dict[str, Any] = {}
