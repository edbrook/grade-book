from ..models import Course, Module, ModuleComponent, GradeBook, Grade
from .util import JsonHandler


class CoursesHandler(JsonHandler):
    def get(self):
        courses = []
        for course in self.session.query(Course):
            courses.append(dict(
                id=course.id,
                name=course.name))
        self.success(dict(courses=courses))
    
    def post(self):
        name = self.json.get('name')
        
        if name is None:
            self.failure("Missing 'name' attribute.")
        else:
            course = Course(name=name)
            self.session.add(course)
            self.session.commit()
            self.success(dict(id=course.id))