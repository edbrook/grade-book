from .handlers import frontend, api
from tornado import web
import os

HANDLERS = [
    (r"/api/v1/courses/?", api.CoursesHandler)
]