from fastapi import FastAPI
from app.api.contact import router as contact_router
from app.api.projects import router as project_router
from app.auth.routes import router as auth_router
from app.auth.dependencies import get_current_admin
from fastapi import Depends

app = FastAPI(
    title="Om Hase Portfolio API"
)

app.include_router(
    contact_router,
    prefix="/contact",
    tags=["Contact"]
)

app.include_router(
    project_router,
    prefix="/projects",
    tags=["Projects"]
)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)


@app.get("/")
def home():
    return {
        "message": "Portfolio API Running"
    }

@app.get("/protected")
def protected_route(
    current_admin: str = Depends(get_current_admin)
):
    return {
        "message": f"Welcome {current_admin}"
    }