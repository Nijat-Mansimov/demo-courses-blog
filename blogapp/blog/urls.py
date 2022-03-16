from unicodedata import name
from django.urls import path
from . import views

# http://127.0.0.1:8000/ = > home page
# http://127.0.0.1:8000/index = > home page
# http://127.0.0.1:8000/blogs = > blogs page
# http://127.0.0.1:8000/blogs/3 = > blogs-details

urlpatterns = [
    path("", views.index, name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("category/<slug:slug>", views.blogs_by_category, name="blogs_by_category"),
    path("blogs/<slug:slug>", views.blog_details, name="blogs_details"),
]
