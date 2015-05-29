from django.http import HttpResponse
from django.template import Template,Context
import datetime
from django.template.loader import get_template


def hello(request):
    return HttpResponse('Hello world!')

def current_datetime(request):
    now = datetime.datetime.now()
    t = get_template('mytemplate.html')
    html = t.render(Context({'current_date':now}))
    return HttpResponse(html)
