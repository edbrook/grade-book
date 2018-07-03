from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml

from gradebook.models import Base, Course, Module, ModuleComponent


def setupDb(data_file):
    engine = create_engine('sqlite:///:memory:', echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    _load_from_file(data_file, session)

    return session


def _load_from_file(data_file, session):
    with open(data_file,'r') as f:
        doc = yaml.load(f)

    for course_data in doc:
        _process_course(course_data, session)

    session.commit()


def _process_course(course_data, session):
    course = Course(name=course_data['name'])
    session.add(course)
    
    module_order = 1
    for module_data in course_data['modules']:
        _process_module(module_data, course, module_order, session)
        module_order += 1        


def _process_module(module_data, course, module_order, session):
    components = module_data.pop('components')
    module = Module(**module_data, ordering=module_order)
    course.modules.append(module)
    session.add(module)

    course_order = 1
    for component_data in components:
        _process_component(component_data, module, course_order, session)
        course_order += 1


def _process_component(component_data, module, course_order, session):
        component = ModuleComponent(**component_data, ordering=course_order)
        module.components.append(component)
        session.add(component)
