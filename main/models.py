from django.db import models
from django.contrib.auth.models import User, AbstractUser


class User(AbstractUser):
    age = models.PositiveIntegerField(default=0) # int default 0
    rating = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True) # numeric(5, 2) 100.00
    saved_posts = models.ManyToManyField('Post', blank=True)    
    def __str__(self) -> str:
        return self.first_name 
    

class Category(models.Model): # main_category
    title = models.CharField(max_length=255)  

    def __str__(self) -> str:
        return self.title  
    


class Tag(models.Model):
    title = models.CharField(max_length=255)  

    def __str__(self) -> str:
        return self.title  


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    # OneToMany relationship
    category = models.ForeignKey(Category, on_delete=models.PROTECT,  null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    image = models.ImageField(upload_to="post_images", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.PositiveIntegerField(default=0)
    dislikes = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)




class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)