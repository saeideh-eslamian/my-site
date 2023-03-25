from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.urls import reverse
from .models import Post, Author, Tag
from django.views import View
from django.views.generic import ListView, DetailView
from .forms import CommentForm
from django.http import HttpResponseRedirect



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

class  PostDetailView(View):

    def save_for_later(self, request, post_id):
        stored_post = request.session.get('stored_post')
        if stored_post is not None:
            is_save_for_later= post_id in stored_post
        else:
            is_save_for_later = False

    def get(self, request, slug):
        post = Post.objects.get(slug=slug)
        comment_form = CommentForm()
        context ={
            'post': post ,
            'post_tag':post.tag.all(),
            'comment_form': comment_form,
            'comments' :post.comments.all().order_by('-id'),
            'save_for_later': is_save_for_later,
         }
        return render(request, 'blog/post-detail.html', context)


    def post(self, request, slug):
        comment_form = CommentForm(request.POST) 
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            response = reverse("post-detail-url", args=[slug])
            
            return HttpResponseRedirect(response)
        
        context = {
            'post': post,
            'post_tag': post.tag.all(),
            'comment_form': comment_form, 
            'comments' :post.comments.all().order_by('-id')
         }
        return render(request, 'blog/post-detail.html', context)

# class  PostDetailView(DetailView):
#     template_name = 'blog/post-detail.html'
#     model = Post
#     context_object_name = 'post'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['post_tags'] = self.object.tag.all() # object = Post.objects.get(slug=slug)
#         context['comment_form'] = CommentForm()
#         return context


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

class ReadLaterView(View):
    def get(self, request):
        stored_post = request.session.get('stored_post')
        context = {}

        if stored_post is None or len(stored_post) == 0:
            context['posts'] = []
            context['has_posts'] = False
        else:   
            posts = Post.objects.filter(id__in=stored_post) 
            context['posts'] = posts
            context['has_posts'] = True

        return render(request, "blog/stored-posts.html", context)    

    def post(self, request):
        stored_post = request.session.get('stored_post')
        if stored_post is None:
            stored_post = []

        post_id = int(request.POST["post-id"])  

        if post_id not in stored_post:
            stored_post.append(post_id)
            request.session['stored_post'] = stored_post

        return HttpResponseRedirect("/")      
