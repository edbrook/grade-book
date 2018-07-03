import json
from tornado.web import RequestHandler, HTTPError


# TODO - rework the handling of Bad Requests etc.
def check_content_type(content_type, expected_type):
    if content_type is None or content_type.lower() != expected_type:
        bad_request = HTTPError()
        bad_request.status_code = 400
        raise bad_request


class JsonHandler(RequestHandler):
    def prepare(self):
        if self.request.method.lower() in ("put", "post"):
            content_type = self.request.headers.get("Content-Type")
            check_content_type(content_type, "application/json")
            self.json = json.loads(self.request.body)
    
    def success(self, data):
        data['status'] = 'ok'
        self.write(data)
        self.finish()
