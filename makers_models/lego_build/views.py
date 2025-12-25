from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.views import generic
from .models import Build, ReviewModel
from .forms import ReviewForm

# Create your views here.

class BuildList(generic.ListView):
    queryset = Build.objects.all()
    template_name = 'build/index.html'
    paginate_by = 10


# def lego_build(request):
#     template = loader.get_template('build.html')
#     return HttpResponse(template.render())

def build_details(request, slug):

    queryset = Build.objects.filter(status=1)
    build = get_object_or_404(queryset, slug=slug)
    review_text = build.comments.all().order_by("-created_on")
    review_count = build.comments.filter(approved=True).count()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review_text = review_form.save(commit=False)
            review_text.author = request.user
            review_text.build = build
            review_text.save()

    review_form = ReviewForm()
    
    context = {
        "build": build,
        "review": review_text,
        "review_count": review_count,
        "review_form": review_form,
    }
    
    return render(
        request,
        "build/Build_detail.html",
        context
    )