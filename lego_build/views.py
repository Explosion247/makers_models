from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponseRedirect
from django.views import generic
from django.contrib import messages
from django.utils.text import slugify
from .models import Build, ReviewModel
from .forms import ReviewForm, BuildForm

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
            messages.add_message(
                request, messages.SUCCESS,
                'Review has been submitted and is waiting for approval'
            )

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
            messages.add_message(request, messages.SUCCESS, 'Review Updated')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review')

        return HttpResponseRedirect(reverse('build_details', args=[slug]))
    
def delete_review(request, slug, comment_id):
    queryset = Build.objects.filter(status=1)
    build = get_object_or_404(queryset, slug=slug)
    review_form = get_object_or_404(ReviewModel, pk=comment_id)
    
    if review_form.author == request.user:
        review_form.delete()
        messages.add_message(request, messages.SUCCESS, 'Review deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own reviews')
    
        return HttpResponseRedirect(reverse('build_details', args=[slug]))
    
def toggle_like(request, slug):
    queryset = Build.objects.filter(status=1)
    build = get_object_or_404(queryset, slug=slug)

    if request.user in build.liked_by.all():
        build.liked_by.remove(request.user)
    else:
        build.liked_by.add(request.user)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def liked_builds(request):
    builds = (
        request.user.liked_builds.filter(status=1)
        if request.user.is_authenticated
        else Build.objects.none()
    )
    user_builds = (
        Build.objects.filter(author=request.user).order_by("-created_on")
        if request.user.is_authenticated
        else Build.objects.none()
    )
    upload_form = BuildForm()
    return render(
        request,
        'build/account.html',
        {
            'builds': builds,
            'user_builds': user_builds,
            'upload_form': upload_form
        }
        )


def build_upload(request):
    if request.method != "POST":
        return redirect('account')

    if not request.user.is_authenticated:
        return redirect('account')

    form = BuildForm(request.POST, request.FILES)
    if form.is_valid():
        build = form.save(commit=False)
        build.author = request.user
        base_slug = slugify(build.title)
        slug = base_slug
        counter = 1
        while Build.objects.filter(slug=slug).exists():
            slug = f"{base_slug}-{counter}"
            counter += 1
        build.slug = slug
        build.status = 1
        build.save()
        messages.add_message(request, messages.SUCCESS, 'Your build has been sucessfully uploaded') 
        return redirect('account')
    else:
        messages.add_message(request, messages.ERROR, 'There has been an Error while uploading your build')

    builds = request.user.liked_builds.filter(status=1)
    return render(
        request,
        'build/account.html',
        {'builds': builds, 'upload_form': form}
    )


def coming_soon(request, section):
    """
    Simple placeholder view for upcoming sections.
    """
    section_title = section.replace('-', ' ').title()
    return render(
        request,
        'build/coming_soon.html',
        {'section': section_title}
    )
