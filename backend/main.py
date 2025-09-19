from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import uvicorn

# Initialize FastAPI app
app = FastAPI(title="Professional Member Directory (PMD)")

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Update with frontend URL in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Pydantic model for profile validation
class Profile(BaseModel):
    id: int
    name: str
    title: str
    bio: str
    skills: List[str]

# Mock data for testing
mock_profiles = [
    Profile(id=1, name="Mayra Harley", title="Enterprise Architect", bio="Ethical AI evangelist", skills=["AI", "Cloud", "Architecture"]),
    Profile(id=2, name="Jordan Lee", title="Data Scientist", bio="Semantic search specialist", skills=["FAISS", "Python", "ML"]),
]

# GET endpoint to retrieve profiles
@app.get("/profiles", response_model=List[Profile])
def get_profiles():
    return mock_profiles

# POST endpoint to create a new profile
@app.post("/profiles", response_model=Profile)
def create_profile(profile: Profile):
    mock_profiles.append(profile)
    return profile

# PUT endpoint to update a profile
@app.put("/profiles/{profile_id}", response_model=Profile)
def update_profile(profile_id: int, updated: Profile):
    for i, p in enumerate(mock_profiles):
        if p.id == profile_id:
            mock_profiles[i] = updated
            return updated
    raise HTTPException(status_code=404, detail="Profile not found")

# Run locally
if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
