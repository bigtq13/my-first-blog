from django.shortcuts import render

# Create your views here.

def hoempage(request):
    return render(request, 'blog/index.html', {})
