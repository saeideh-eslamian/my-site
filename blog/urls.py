from django.urls import path
from . import views

urlpatterns = [
    # path('',views.index, name='index-url'),
    path('',views.indexView.as_view(), name='index-url'),
    # path('posts/', views.posts, name='posts-url'),
    path('posts/', views.postsView.as_view(), name='posts-url' ),
    # path('posts/<slug:slug>', views.post_detail, name='post-detail-url'),
    path("posts/<slug:slug>/", views.PostDetailView.as_view(), name="post-detail-url" ),
    path('read-later/', views.ReadLaterView.as_view(), name ="read-later"),
]
