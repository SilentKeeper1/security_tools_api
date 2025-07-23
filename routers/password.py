from fastapi import APIRouter
import secrets
import string

router = APIRouter()

@router.get("/password")
async def generate_password():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(12))
    return {"password": password}