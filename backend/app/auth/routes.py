from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Admin

from app.schemas.auth import LoginRequest

from app.auth.security import verify_password
from app.auth.jwt_handler import create_access_token

router = APIRouter()


@router.post("/login")
def login(
    request: LoginRequest,
    db: Session = Depends(get_db)
):

    admin = db.query(Admin).filter(
        Admin.username == request.username
    ).first()

    if not admin:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    if not verify_password(
        request.password,
        admin.password_hash
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )

    token = create_access_token(
        {
            "sub": admin.username
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }