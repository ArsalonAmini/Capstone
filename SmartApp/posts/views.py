from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .forms import PostForm
from .models import Post


def posts_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "success")
        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not success")
    context = {
            "form": form,
    }
    return render(request, "post_form.html", context)


def posts_update(request, id=None):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "<a href='#'>Item </a> Saved", extra_tags='html_safe')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def posts_delete(request, id=None):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    messages.success(request, "successfully deleted")
    return redirect("posts:list")


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

    return render(request, "index.html", context)





