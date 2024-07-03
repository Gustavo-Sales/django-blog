from django.urls import path, include

from . import views


app_name = "blog"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("tinymce/", include("tinymce.urls")),
]
