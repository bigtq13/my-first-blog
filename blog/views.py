from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post
from .form import PostForm

# Create your views here.

def homepage(request):
    return render(request, 'blog/index.html', {})

def eipT(request):
    return render(request, 'blog/projects/eipT.html', {})

def chtgstoreT(request):
    return render(request, 'blog/projects/chtgstoreT.html', {})

def chtselfserviceT(request):
    return render(request, 'blog/projects/chtselfserviceT.html', {})

def amrtT(request):
    return render(request, 'blog/projects/amrtT.html', {})

def visualizationCorner(request):
    return render(request, 'blog/projects/visualizationDesign/visualizationCorner.html', {})

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/projects/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/projects/post_detail.html', {'post': post})

def post_new(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/projects/post_edit.html', {'form': form})

def post_edit(request, pk):
    post=get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'blog/projects/post_edit.html', {'form': form})
