from django.shortcuts import render
from django.views.generic import TemplateView


# Create your views here.

class HelloWorldPageView(TemplateView):
    template_name = 'hello_world.html'