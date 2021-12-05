from django.contrib import admin
from user.models import MyUser, Post
# Register your models here.

@admin.register(MyUser)
class AdminMyUser(admin.ModelAdmin):
    list_display = ['username', 'email', 'password']


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['user', 'text']
