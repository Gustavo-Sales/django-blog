from django.views import generic

from .models import Post


class Index(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-pub_date")
    context_object_name = "latest_posts_list"
    template_name = "index.html"
