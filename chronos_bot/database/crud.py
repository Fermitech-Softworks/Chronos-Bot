from enum import Enum

from sqlalchemy.orm.session import Session
from chronos_bot.database.models import User, Course, Room, Building, Lesson


class UserSearchEnum(Enum):
    UID = 0
    USERNAME = 1
    CHATID = 2


def add(db: Session, object):
    db.add(object)
    db.commit()
    db.refresh(object)
    return object


def create_user(db: Session, username: str, chat_id: str):
    new_user = User(username=username, chat_id=chat_id)
    return add(db, new_user)


def get_user(db: Session, mode: int, search):
    if mode == UserSearchEnum.UID:
        return db.query(User).filter_by(uid=search).first()
    if mode == UserSearchEnum.USERNAME:
        return db.query(User).filter_by(username=search).first()
    if mode == UserSearchEnum.CHATID:
        return db.query(User).filter_by(chat_id=search).first()
    raise Exception


def update_user(db: Session, mode: int, search, username: str, chat_id:str):
    user: User = get_user(db, mode, search)
    user.username = username
    user.chat_id = chat_id
    db.commit()
    return user

