from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import yaml

from gradebook.models import Base, Course, Module, ModuleComponent


def setupDb(source_data):
    engine = create_engine('sqlite:///:memory:', echo=False)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    with open(source_data,'r') as f:
        doc = yaml.load(f)

    for c in doc:
        course = Course(name=c['name'])
        session.add(course)
        m_order = 1
        for m in c['modules']:
            _process_module(m, course, m_order, session)
            m_order += 1
        session.commit()

    return session


def _process_module(m, course, m_order, session):
    components = m.pop('components')
    module = Module(**m, ordering=m_order)
    course.modules.append(module)
    session.add(module)
    c_order = 1
    for co in components:
        _process_component(co, module, c_order, session)
        c_order += 1


def _process_component(co, module, c_order, session):
        component = ModuleComponent(**co, ordering=c_order)
        module.components.append(component)
        session.add(component)
