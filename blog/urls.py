from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post.detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(), name='post.update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post.delete'),
    path('post/create', PostCreateView.as_view(), name='post.create'),
    # rest of routes
    path('about', views.about, name='about'),
]
