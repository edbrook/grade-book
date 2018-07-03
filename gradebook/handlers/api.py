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


class CourseHandler(JsonHandler):
    def get(self, course_id):
        course = self.session.query(Course) \
                        .filter(Course.id == course_id) \
                        .first()
        if course is not None:
            modules = list(map(lambda m: m.id, course.modules))
            course = dict(
                id=course.id,
                name=course.name,
                modules=modules)
            self.success(dict(course=course))
        else:
            self.send_error(404, reason='No such course!')