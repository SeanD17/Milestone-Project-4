from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    Return all posts that are with status 1 (published) and order from the latest one.
    """
    queryset = Post.objects.filter(status=1).order_by('title')
    template_name = 'blog/blog.html'

