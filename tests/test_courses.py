import unittest

from .utils import setupDb
from gradebook.models import Base, Course, Module, ModuleComponent


class TestCourseModels(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.session = setupDb('tests/courses.yaml')

    @classmethod
    def tearDownClass(cls):
        cls.session.close()
    
    def test_get_course_name(self):
        cs = self.session.query(Course).first()
        self.assertEqual(cs.name, 'MEng Computer Science')
    
    def test_get_course_modules(self):
        cs = self.session.query(Course).first()
        mods = cs.modules
        self.assertEqual(len(mods), 2)