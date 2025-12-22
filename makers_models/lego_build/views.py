from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Build
# Create your views here.

class LegoList(generic.ListView):
    queryset = Build.objects.all()
    template_name = 'build/index.html'


# def lego_build(request):
#     template = loader.get_template('build.html')
#     return HttpResponse(template.render())

def build_details(request, slug):

    queryset = Build.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "build/index.html",
        {"post": post}
    )