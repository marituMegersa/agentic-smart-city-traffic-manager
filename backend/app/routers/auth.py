from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/api/v1/auth", tags=["Authentication"])

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(data: LoginRequest):
    if data.username and data.password:
        return {"access_token": f"mock_jwt_token_{data.username}", "token_type": "bearer"}
    raise HTTPException(status_code=400, detail="Invalid credentials")
