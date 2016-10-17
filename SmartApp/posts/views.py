from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from .models import Post


def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
            "form": form,
    }
    return render(request, "post_form.html", context)


def posts_detail(request, id=None):
    instance = get_object_or_404(Post, id=id)
    context = {
        "title": "Detail",
        "instance": instance
    }
    return render(request, "post_detail.html", context)


def posts_list(request):
    queryset = Post.objects.all()
    context = {
            "object_list": queryset,
            "title": "My user List"
    }

    # if request.user.is_authenticated():
    #     context = {
    #         "title": "My user List"
    #     }
    # else:
    #     context = {
    #         "title": "List"
    #     }
    return render(request, "index.html", context)


def posts_update(request):
    context = {
        "title": "Update"
    }
    return render(request, "index.html", context)


def posts_delete(request):
    context = {
        "title": "Delete"
    }
    return render(request, "index.html", context)


