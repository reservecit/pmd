from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import profiles # tells Python to start from the top-level backend package and drill down (absolute import inside main.py)
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
