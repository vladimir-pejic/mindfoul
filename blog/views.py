from django.shortcuts import render
from django.http import HttpResponse


posts = [
    {
        'author': 'Vladimir',
        'title': 'Post 1',
        'content': 'Blalasdlsapdasd laspd laspd laspd asdaisjd asidj asidj asid',
        'created_at': '2019-02-11 13:03:03'
    },
    {
        'author': 'Dare',
        'title': 'Post 2',
        'content': 'Blalasdlsapdasd laspd laspd laspd asdaisjd asidj asidj asid',
        'created_at': '2019-02-11 13:04:03'
    },
    {
        'author': 'Milinko',
        'title': 'Post 3',
        'content': 'Blalasdlsapdasd laspd laspd laspd asdaisjd asidj asidj asid',
        'created_at': '2019-02-11 13:05:03'
    },
]

# Create your views here.
def index(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)

def about(request):
    return render(request, 'blog/about.html')

def create(request):
    return render(request, 'blog/create.html')
