from django.shortcuts import render

# Create your views here.from django.shortcuts import render
from blog.models import Post, Comment
from .forms import CommentForm

def blog_index(req):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }
    return render(req, "blog_index.html", context)

def blog_category(req, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(req, "blog_category.html", context)


def blog_detail(req, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if req.method == 'POST':
        form = CommentForm(req.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(req, "blog_detail.html", context)