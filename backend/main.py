from fastapi import FastAPI
from backend.routes import profiles
from fastapi.middleware.cors import CORSMiddleware
from db.database import Base, engine

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI()  # removed title="PMD Directory" from FastAPI(title="PMD Directory")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5500"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(profiles.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)
#    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
