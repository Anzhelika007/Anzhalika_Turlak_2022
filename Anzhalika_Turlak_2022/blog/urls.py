from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.problog_index, name="blog_index"),
    path("<int:blog_id>/", views.blog_detail, name="blog_detail"),
]