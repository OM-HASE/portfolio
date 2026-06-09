from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.models import Contact

from app.schemas.contact import ContactCreate

router = APIRouter()


@router.post("/")
def create_contact(
    contact: ContactCreate,
    db: Session = Depends(get_db)
):

    new_contact = Contact(
        name=contact.name,
        email=contact.email,
        company=contact.company,
        message=contact.message
    )

    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

    return {
        "message": "Contact submitted successfully"
    }