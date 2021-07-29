from django.contrib import admin

# Register your models here.
from blogApp.models import BlogModel, Profile

admin.site.register(BlogModel)
admin.site.register(Profile)