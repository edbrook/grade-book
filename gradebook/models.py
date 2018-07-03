from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.schema import Table, Column, ForeignKey
from sqlalchemy.types import SmallInteger, Integer, String
from sqlalchemy.ext.declarative import declarative_base

from .settings import settings


__all__ = ['Course', 'Module', 'ModuleComponent', 'GradeBook', 'Grade']


Base = declarative_base()
Session = sessionmaker()

course_module_table = Table('course_module', Base.metadata,
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('module_id', Integer, ForeignKey('module.id')))


def get_db_engine(url, echo=False):
    engine = create_engine(url, pool_recycle=300, echo=echo)
    Base.metadata.create_all(engine)
    return engine


class Course(Base):
    __tablename__ = 'course'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    modules = relationship('Module', secondary=course_module_table)

    def __repr__(self):
        return f'Course(name="{self.name}")'


class Module(Base):
    __tablename__ = 'module'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(SmallInteger)
    ordering = Column(SmallInteger)
    components = relationship('ModuleComponent',
        backref='module')


class ModuleComponent(Base):
    __tablename__ = 'module_component'

    id = Column(Integer, primary_key=True)
    module_id = Column(Integer, ForeignKey('module.id'))
    name = Column(String)
    ordering = Column(SmallInteger)
    weighting = Column(Integer)


class GradeBook(Base):
    __tablename__ = 'grade_book'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)


class Grade(Base):
    __tablename__ = 'grade'

    id = Column(Integer, primary_key=True)
    component = Column(Integer, ForeignKey('module_component.id'))
    score = Column(Integer)
