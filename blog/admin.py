from django.contrib import admin
from .models import Post, Tag, Author, Comment

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','date','author')
    list_filter = ('date','author')

class CommentAdmin(admin.ModelAdmin):
    list_display=('user_name','post')    


admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment,CommentAdmin)
