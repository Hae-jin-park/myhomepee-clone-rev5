from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.views.generic import DetailView

from .models import Post


# Create your views here.
@login_required
def index(request):
    post_list = Post.objects.all()
    return render(request, "blog/index.html", {"post_list": post_list})

class PostDetailView(DetailView):
    model = Post
    template_name="blog/blog_detail.html"


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/blog_detail.html",{
        "post":post,
    })