from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import profiles
from db.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="PMD Directory")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(profiles.router)
