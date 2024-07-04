from django.views import generic

from .models import Post


class Index(generic.ListView):
    model = Post
    queryset = Post.objects.all().order_by("-pub_date")
    context_object_name = "latest_posts_list"
    template_name = "index.html"


class DetailPost(generic.DetailView):
    model = Post
    template_name = "detail_post.html"


class SearchPosts(generic.ListView):
    model = Post
    context_object_name = "filtered_posts"
    template_name = "post_search.html"

    def get_queryset(self):
        query = self.request.GET.get("q")
        if query:
            return Post.objects.filter(title__icontains=query)
        return Post.objects.none()
