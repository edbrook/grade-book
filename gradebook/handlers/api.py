from .util import JsonHandler


class CoursesHandler(JsonHandler):
    def get(self):
        self.success(dict(courses=[]))
    
    def post(self):
        print(self.json)
        self.success({})