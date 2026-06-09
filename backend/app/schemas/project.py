from pydantic import BaseModel


class ProjectCreate(BaseModel):
    title: str
    description: str

    github_url: str
    demo_url: str

    tech_stack: str
    featured: bool = False