from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Post
# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.all()
    template_name = 'build/index.html'
    paginate_by = 6


# def lego_build(request):
#     template = loader.get_template('build.html')
#     return HttpResponse(template.render())

def build_details(request, slug):

    queryset = Post.objects.filter(status=1)
    # post = get_object_or_404(queryset, slug=slug)
    context = {
        "post": queryset
    }

    return render(
        request,
        "build/build.html",
        context
    )