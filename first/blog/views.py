from django.shortcuts import render, HttpResponse
from .models import Post
# Create your views here.

def home(request):
    # print(Post.objects.all)
    # return HttpResponse("Bienvenidos a nuestra web")
    posts = Post.objects.all()
    return render(request, "blog/home.html", {'posts' : posts} )