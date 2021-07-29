from django.db import models
from django.contrib.auth.models import User
from froala_editor.fields import FroalaField
from .helpers import generate_slug, generate_random_string


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False)
    token = models.CharField(max_length=100)


class BlogModel(models.Model):
    title = models.CharField(max_length=1000)  # title name
    content = FroalaField()
    slug = models.SlugField(max_length=1000, null=True, blank=True)  # selection filed
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='blogpics')
    created_at = models.DateTimeField(auto_now_add=True)  # register timestamp of the blog created
    upload_to = models.DateTimeField(auto_now=True)  # register timestamp of the blog when updated

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = generate_slug(self.title)
        super(BlogModel, self).save(*args, **kwargs)
