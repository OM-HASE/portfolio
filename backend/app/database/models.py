from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy import Boolean
from sqlalchemy import DateTime

from datetime import datetime

from app.database.database import Base


class Contact(Base):
    __tablename__ = "contacts"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String(100))
    email = Column(String(150))
    company = Column(String(150))
    message = Column(Text)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)

    title = Column(String(200))
    description = Column(Text)

    github_url = Column(String(300))
    demo_url = Column(String(300))

    tech_stack = Column(Text)

    featured = Column(
        Boolean,
        default=False
    )

class Admin(Base):
    __tablename__ = "admins"

    id = Column(Integer, primary_key=True, index=True)

    username = Column(String(100), unique=True, nullable=False)

    password_hash = Column(String(255), nullable=False)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )