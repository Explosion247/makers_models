from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views import generic
from .models import Build
# Create your views here.

class LegoList(generic.ListView):
    queryset = Build.objects.filter(status=1)
    template_name = 'build/index.html'

# def lego_build(request):
#     template = loader.get_template('build.html')
#     return HttpResponse(template.render())
