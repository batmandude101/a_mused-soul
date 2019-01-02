from django.shortcuts import render
from django.http import HttpResponse
from .models import post
# Create your views here.
posts = [
    {
        'author': 'saksham',
        'title' : 'My first blog',
        'content': 'in development',
        'date_posted':'29 dec 2018',

    },
    {
        'author': 'ashu',
        'title' : 'just a while',
        'content': 'beautiful',
        'date_posted':'29 dec 2018',

    },

]

def home(request):
    context ={
        'posts': post.objects.all()
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title': 'About'})
