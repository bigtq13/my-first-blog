from django.shortcuts import render

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
