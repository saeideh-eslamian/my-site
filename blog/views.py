from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Post, Author, Tag
from django.views import View
from django.views.generic import ListView, DetailView


# class indexView(View):
#     def get(self, request):
#         latest_posts = Post.objects.all().order_by('-date')[:3]
#         return render(request,'blog/index.html',{
#         'posts':latest_posts})
    
class  indexView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts' 
    ordering = ['-date']

    def get_queryset(self):
        basequery = super().get_queryset()
        data = basequery[:3]
        return data
    



# def index(request):
#     latest_posts = Post.objects.all().order_by("-date")[:3]

#     return render(request,'blog/index.html',{
#         'posts':latest_posts})

class postsView(ListView):
    template_name = 'blog/posts.html'
    model = Post
    context_object_name = 'all_posts'
    ordering = ['-date']
           


# def posts(request):
#     all_posts = Post.objects.all().order_by('date')
    
#     return render(request,'blog/posts.html',{'all_posts':all_posts})

class  PostDetailView(DetailView):
    template_name = 'blog/post-detail.html'
    model = Post
    context_object_name = 'post'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['post_tags'] = self.object.tag.all() # object = Post.objects.get(slug=slug)
        return context


# def post_detail(request, slug):
#     try:
#         post = Post.objects.get(slug=slug)
#         return render(request,'blog/post-detail.html',{
#             'post':post,
#             'post_tags':post.tag.all()
#         })
#     except: 
#         raise Http404()  
    
#     post=get_object_or_404(Post,slug=slug) #secund method

