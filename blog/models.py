from django.db import models
from django.core.validators import MinLengthValidator

class Tag(models.Model):
    caption = models.CharField(max_length=50)

    def __str__(self):
        return self.caption

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(null=True)

    def fullName(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.fullName()


class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image_name = models.CharField(max_length=80)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True, db_index=True, null=False)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,on_delete=models.SET_NULL, null=True, related_name='posts')
    tag = models.ManyToManyField(Tag, null=True)

    def __str__(self): 
        return f"{self.title} ({self.date})"
    
    class Meta:
        verbose_name_plural = "All Posts"

