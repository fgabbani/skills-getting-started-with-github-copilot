from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError
from pydantic import BaseModel

from app.auth import create_access_token, decode_access_token

app = FastAPI(title="Backend JWT API")

VALID_USERNAME = "admin"
VALID_PASSWORD = "admin123"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class Token(BaseModel):
    access_token: str
    token_type: str


@app.post("/token", response_model=Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != VALID_USERNAME or form_data.password != VALID_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token(data={"sub": form_data.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/token/refresh", response_model=Token)
async def refresh_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = decode_access_token(token)
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    new_token = create_access_token(data={"sub": payload["sub"]})
    return {"access_token": new_token, "token_type": "bearer"}
