import json
from tornado.web import RequestHandler, HTTPError

from .. import models


# TODO - rework the handling of Bad Requests etc.
def check_content_type(content_type, expected_type):
    if content_type is None or content_type.lower() != expected_type:
        bad_request = HTTPError()
        bad_request.status_code = 400
        raise bad_request


class BaseHandler(RequestHandler):
    def initialize(self):
        super(BaseHandler, self).initialize()
        my_settings = self.application.my_settings
        if my_settings.get("db_engine") is None:
            engine = models.get_db_engine(my_settings.get("db_uri"))
            models.Session.configure(bind=engine)
            my_settings["db_engine"] = engine
            my_settings["db_session"] = models.Session

        self.engine = my_settings.get("db_engine")
        self.session = my_settings.get("db_session")()
    
    def on_finish(self):
        self.session.close()



class JsonHandler(BaseHandler):
    def prepare(self):
        if self.request.method.lower() in ("put", "post"):
            content_type = self.request.headers.get("Content-Type")
            check_content_type(content_type, "application/json")
            self.json = json.loads(self.request.body)
    
    def success(self, data={}):
        data['status'] = 'ok'
        self.write(data)
        self.finish()
    
    def failure(self, msg=None):
        msg = msg or "Error"
        self.send_error(400, reason=msg)
