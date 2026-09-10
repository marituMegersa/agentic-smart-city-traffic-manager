class AgentExecutionError(Exception):
    def __init__(self, message: str, agent_name: str):
        self.message = message
        self.agent_name = agent_name
        super().__init__(f"[{agent_name}] {message}")
