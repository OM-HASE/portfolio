from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Project

from app.schemas.project import ProjectCreate

router = APIRouter()


@router.post("/")
def create_project(
    project: ProjectCreate,
    db: Session = Depends(get_db)
):

    new_project = Project(
        title=project.title,
        description=project.description,
        github_url=project.github_url,
        demo_url=project.demo_url,
        tech_stack=project.tech_stack,
        featured=project.featured
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return new_project


@router.get("/")
def get_projects(
    db: Session = Depends(get_db)
):
    return db.query(Project).all()