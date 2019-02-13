from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Post

# Create your views here.
def index(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html')

@login_required
def create(request):
    return render(request, 'blog/create.html')
