from sqlalchemy import Column, Integer, String, ARRAY
from db.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    title = Column(String)
    bio = Column(String)
    skills = Column(ARRAY(String))  # PostgreSQL array type
