from pathlib import Path

from django.http import HttpResponse
from django.views.generic import TemplateView


def hello_world_function(request):
    object = HttpResponse('<h1>Hello World!<h1>')
    return object


class HelloWorldClass(TemplateView):
    template_name = 'hello.html'


def some_view(request):
    print(Path(__file__).resolve().parent.parent)
    return HttpResponse('')
