from django.urls import path, include
from django.views.generic import ListView, DetailView
from blog.models import Post

urlpatterns = [
	path('', ListView.as_view(queryset=Post.objects.all().order_by("-date")),name="blog/blog.html")
]