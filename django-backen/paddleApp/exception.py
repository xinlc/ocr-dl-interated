import json

from django.http import HttpResponse


class CustomException:
  '''
      自定义错误
  '''

  def __init__(self, msg):
    self.status = 503
    self.msg = msg

  def get(self):
    return HttpResponse(json.dumps({'message': self.msg, 'data': None, "code": self.status}),
                        status=400,
                        content_type="application/json")
