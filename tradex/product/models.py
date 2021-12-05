from django.db import models


# Create your models here.
# 2. Products app with Product model. Product : name, weight, price, created_at, updated_at Both of the apps should use two different databases. 
# Create a form that an authenticated user can use to create a post.

#  Note:
# 1. Register all models on the admin dashboard.
# 2.Please upload your assignment on GitHub and share me the GitHub link at shreya@tradexa.co.in
# 3. Please  mail your resume on shreya@tradexa.co.in

class Product(models.Model):
    name = models.CharField(max_length=226)
    weight = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
