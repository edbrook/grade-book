from .handlers import frontend, api
from tornado import web
import os

HANDLERS = [
    (r"/api/v1/courses/?", api.CoursesHandler),
    (r"/api/v1/courses/(?P<course_id>\d{1,4})/?", api.CourseHandler)
]