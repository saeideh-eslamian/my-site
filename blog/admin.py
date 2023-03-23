from django.contrib import admin
from .models import Post, Tag, Author

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('title',)}
    list_display = ('title','date','author')
    list_filter = ('date','author')


admin.site.register(Post,PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
