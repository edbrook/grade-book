from sqlalchemy import (Table, Column, SmallInteger, Integer,
    String, ForeignKey)
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


course_module_table = Table('course_module', Base.metadata,
    Column('course_id', Integer, ForeignKey('course.id')),
    Column('module_id', Integer, ForeignKey('module.id')))


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
