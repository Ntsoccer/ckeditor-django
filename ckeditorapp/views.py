from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Post
from .forms import PostForm
from django.views.generic import TemplateView, CreateView, DetailView, UpdateView, DeleteView, ListView


def index(request):
    post = Post.objects.order_by('-id')
    return render(request, 'ckeditorapp/index.html', {'post': post})


def detail(request, post_id):
    post_text = get_object_or_404(Post, id=post_id)
    return render(request, 'ckeditorapp/detail.html', {'post_text': post_text})


def add_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('ckeditorapp:index')

    else:
        form = PostForm

    return render(request, 'ckeditorapp/form.html', {'form': form})
