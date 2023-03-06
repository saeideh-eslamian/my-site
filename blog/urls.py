from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index-url'),
    path('posts/',views.posts, name='posts-url'),
    path('posts/<slug:slug>', views.post_detail, name='post-detail-url'),
]
