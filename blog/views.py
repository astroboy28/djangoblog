from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post
from django.shortcuts import render, get_object_or_404

def post_list(request):
    posts = Post.objects.filter(status='published').order_by('-created_at')
    paginator = Paginator(posts, 6)  # Show 6 posts per page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'page_obj': page_obj})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    return render(request, 'blog/post_detail.html', {'post': post})


def about(request):
    return render(request, "blog/about.html", {"team": "DjangoBlog Team"})

def contact(request):
    return render(request, "blog/contact.html", {"banana": "DjangoBlog Contact"})