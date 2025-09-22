from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import SessionLocal # changed back from... from backend.db.database import SessionLocal
from models.profile import Profile as DBProfile
from pydantic import BaseModel
from typing import List

router = APIRouter()

# Pydantic model
class ProfileSchema(BaseModel):
    id: int
    name: str
    title: str
    bio: str
    skills: List[str]

    class Config:
        orm_mode = True

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET /profiles
@router.get("/profiles") # changed from... @router.get("/profiles", response_model=List[ProfileSchema])
def get_profiles():  # changed from... get_profiles(db: Session = Depends(get_db))
    return {"message": "Profiles endpoint is working"}
    # return db.query(DBProfile).all()

# POST /profiles
@router.post("/profiles", response_model=ProfileSchema)
def create_profile(profile: ProfileSchema, db: Session = Depends(get_db)):
    db_profile = DBProfile(**profile.dict())
    db.add(db_profile)
    db.commit()
    db.refresh(db_profile)
    return db_profile
