from sqlalchemy import Integer, String, LargeBinary, Column, Boolean, ForeignKey, SmallInteger, DateTime, JSON, Float, \
    Table
from sqlalchemy.orm import relationship
from .db import Base

attends_table = Table('attends', Base.metadata,
                      Column('user_id', ForeignKey('user.uid'), primary_key=True),
                      Column('course_id', ForeignKey('course.cid'), primary_key=True)
                      )


class User(Base):
    __tablename__ = "user"

    uid = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    chat_id = Column(String, unique=True)

    courses = relationship("Course", secondary=attends_table, backref="users")


class Course(Base):
    __tablename__ = "course"

    cid = Column(Integer, primary_key=True, autoincrement=True)
    professor = Column(String, nullable=False)
    cfu = Column(Integer, nullable=False)
    code = Column(String, unique=True, nullable=False)
    online = Column(Boolean, default=False, nullable=False)
    online_url = Column(String)


class Building(Base):
    __tablename__ = "building"

    bid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    city = Column(String, nullable=False)
    lat = Column(Float)
    lng = Column(Float)
    last_change = Column(DateTime, nullable=False)
    complex = Column(String)
    code = Column(String, nullable=False, unique=True)

    rooms = relationship("Room", back_populates="building")


class Room(Base):
    __tablename__ = "room"

    rid = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    floor = Column(String)
    capacity = Column(Integer)
    last_change = Column(DateTime, nullable=False)
    services = Column(JSON)
    code = Column(String, nullable=False, unique=True)

    bid = Column(Integer, ForeignKey("building.bid"))
    building = relationship(Building, back_populates="rooms")


class Lesson(Base):
    __tablename__ = "lesson"

    lid = Column(Integer, primary_key=True, autoincrement=True)
    cid = Column(Integer, ForeignKey("course.cid"), primary_key=True)
    rid = Column(Integer, ForeignKey("room.rid"), primary_key=True)
    last_change = Column(DateTime, nullable=False)
    start = Column(DateTime, nullable=False)
    end = Column(DateTime, nullable=False)

    course = relationship("Course", backref="lessons")
    room = relationship("Room", backref="lessons")
