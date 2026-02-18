from django.db import models
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class author(models.Model):
    first_name = models.CharField(max_length=50)
    Second_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True, null=True)
    def __str__(self):
        return f"{self.first_name} {self.Second_name}"
class tag(models.Model):
    caption = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.caption

class Blogs(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blogs/')
    date = models.DateField(db_index=True)
    content = models.TextField()
    author = models.ForeignKey(author, on_delete=models.SET_NULL,related_name='posts', null=True)
    tags = models.ManyToManyField(tag)
    slug = models.SlugField(unique=True)
    class Meta:
        verbose_name_plural = "blog posts"
    
    def __str__(self):
        return self.title
class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    user_email = models.EmailField(max_length=254)
    text = models.TextField()
    post = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments')
    def __str__(self):
        return f"{self.user_name} - {self.post.title}"