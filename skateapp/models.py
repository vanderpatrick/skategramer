# All necessary imports

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from cloudinary.models import CloudinaryField
from django.utils.timezone import timezone
from ckeditor.fields import RichTextField


# All app models.

# post model responsible for regular post made by (user/admin)
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image', eager=[{'width': '400', 'height': '400', 'crop':'crop'}], transformation={'width': '400', 'height': '400', 'crop':'fill', 'radius':'20'})
    content = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User,related_name='blogpost_like',)

    def num_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home')
    def save(self, *args, **kwargs):
        super().save()

    def __str__(self):
        return self.title

# Comment model responsible for regular comments in Post model by (user/admin)
class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.user.username} Comment'

# Profile model responsible for the creation and maintance of the user profile by (user/admin)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = CloudinaryField('image')
    description = RichTextField(blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True, null=True)
    # description = models.TextField(max_length=300)
    

    def __str__(self):
        return f'{self.user.username} profile'
    
    def save(self, *args, **kwargs):
        super().save()

# PostTutorial model responsible for the tutorial post made only by (admin)
class PostTutorial(models.Model):
    title = models.CharField(max_length=200, unique=True)
    image = CloudinaryField('image')
    description = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    update_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title