from celery import Celery
import os

redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
celery_app = Celery("agent_tasks", broker=redis_url, backend=redis_url)

@celery_app.task
def execute_background_agent_task(task_id: str, prompt: str):
    return {"task_id": task_id, "status": "COMPLETED", "result": f"Executed agent trajectory for '{prompt}'"}
