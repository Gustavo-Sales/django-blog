from django.views import generic

from .models import Post


class Index(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-pub_date")
