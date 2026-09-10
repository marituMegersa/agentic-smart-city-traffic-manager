from app.models.state import AgentState

class AgentOrchestrator:
    def __init__(self, name: str = "agentic-smart-city-traffic-manager"):
        self.name = name

    def plan_execution(self, prompt: str) -> AgentState:
        state = AgentState(task_id="TASK-1001")
        state.history.append({"step": "PLANNING", "detail": f"Generated trajectory plan for query: {prompt}"})
        return state
