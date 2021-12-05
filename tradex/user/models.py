from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# first_name, last_name, email, password, username
# Post : user, text, created_at, updated_at Foreign key relationship exists between User and Post on Model level not on Database level. 


class MyUser(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True, db_index=True)
    email = models.EmailField(max_length=255, unique=True, db_index=True)
    password = models.CharField(max_length=22)
    
class Post(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    text = models.CharField(max_length=501)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)