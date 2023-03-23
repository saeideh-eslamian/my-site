from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Author, Tag


def index(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]

    return render(request,'blog/index.html',{
        'posts':latest_posts})

def posts(request):
    all_posts = Post.objects.all().order_by('date')
    
    return render(request,'blog/posts.html',{'all_posts':all_posts})

def post_detail(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        return render(request,'blog/post-detail.html',{
            'post':post,
            'post_tags':post.tag.all()
        })
    except: 
        raise Http404()  
    
    #post=get_object_or_404(Post,slug=slug) #secund method

