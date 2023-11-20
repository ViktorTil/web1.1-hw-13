from sqlalchemy.orm import Session
from sqlalchemy import and_
from src.database.models import Contact, User
from src.schemas import ContactModel


async def get_contacts(user: User, db: Session):
    return db.query(Contact).filter(Contact.user_id == user.id).all()



async def get_contact_by_id(contact_id: int, user: User, db: Session):
    contact = db.query(Contact).filter_by(id=contact_id).first()
    return contact


async def get_contact_by_email(contact_email: str, user: User, db: Session):
    contact = db.query(Contact).filter(and_(Contact.email==contact_email, Contact.user_id == user.id)).first()
    return contact

async def get_contact_first_name(first_name: str, user: User, db: Session):
    contact = db.query(Contact).filter_by(first_name=first_name).first()
    return contact


async def get_contact_last_name(last_name: str, user: User, db: Session):
    contact = db.query(Contact).filter_by(last_name=last_name).first()
    return contact


async def create(body: ContactModel, user: User, db: Session):
    contact = Contact(**body.dict(), user = user)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact


async def update(contact_id: int, body: ContactModel, user: User, db: Session):
    contact = await get_contact_by_id(contact_id, user, db)
    if contact:
        contact.first_name = body.first_name
        contact.last_name = body.last_name
        contact.email = body.email
        contact.phone = body.phone
        contact.birthday = body.birthday
        db.commit()
    return contact


async def remove(contact_id: int, user: User, db: Session):
    contact = await get_contact_by_id(contact_id, user, db)
    if contact:
       db.delete(contact)
       db.commit()
    return contact