from django.urls import path, include

from . import views


app_name = "blog"
urlpatterns = [
    path("", views.Index.as_view(), name="index"),
    path("post/<int:pk>/", views.DetailPost.as_view(), name="post"),
    path("pesquisa/", views.SearchPosts.as_view(), name="search"),
    path("tinymce/", include("tinymce.urls")),
]
