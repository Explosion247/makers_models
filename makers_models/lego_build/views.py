from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
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
    reviews = build.comments.all().order_by("-created_on")
    
    review_count = build.comments.filter(approved=True).count()
    review_form = ReviewForm()

    if request.method == "POST":
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.author = request.user
            review.build = build
            review.save()

    context = {
        "build": build,
        "reviews": reviews,
        "review_count": review_count,
        "review_form": review_form,
    }
    
    return render(
        request,
        "build/build_detail.html",
        context
    )

def review_edit(request, slug, comment_id):

    if request.method == "POST":
        queryset = Build.objects.filter(status=1)
        build = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(ReviewModel, pk=comment_id)
        review_form = ReviewForm(data=request.POST, instance=review)

        if review_form.is_valid() and review.author == request.user:
            review = review_form.save(commit=False)
            review.build = build
            review.approved = False
            review.save()

        return HttpResponseRedirect(reverse('build_details', args=[slug]))
    
def delete_review(request, slug, comment_id):
    queryset = Build.objects.filter(status=1)
    build = get_object_or_404(queryset, slug=slug)
    review_form = get_object_or_404(ReviewModel, pk=comment_id)
    if review_form.author == request.user:
        review_form.delete()
    
        return HttpResponseRedirect(reverse('build_details', args=[slug]))