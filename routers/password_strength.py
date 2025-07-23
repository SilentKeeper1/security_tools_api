from fastapi import APIRouter
from pydantic import BaseModel
import string

router = APIRouter()

class PasswordInput(BaseModel):
    password: str

@router.post("/password_strength")
async def password_strength(input: PasswordInput):
    password = input.password
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in string.punctuation for c in password):
        score += 1

    if score <= 2:
        strength = "Weak"
    elif score == 3 or score == 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return {"strength": strength, "score": score}