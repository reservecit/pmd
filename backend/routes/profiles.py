from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.db.database import SessionLocal    # ← now under backend.db
from models.profile import Profile as DBProfile
from pydantic import BaseModel
from typing import List

router = APIRouter()

class ProfileSchema(BaseModel):
    id: int
    name: str
    title: str
    bio: str
    skills: List[str]

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/profiles")
def get_profiles():    
    return {"message": "Profiles endpoint is working"}

@router.post("/profiles", response_model=ProfileSchema)
def create_profile(profile: ProfileSchema, db: Session = Depends(get_db)):
    db_profile = DBProfile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
