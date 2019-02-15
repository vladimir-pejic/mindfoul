from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView
                                  )
from django.http import HttpResponse
from .models import Post


def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class PostDetailView(DetailView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)




def about(request):
    return render(request, 'blog/about.html')


@login_required
def create(request):
    return render(request, 'blog/post_form.html')
