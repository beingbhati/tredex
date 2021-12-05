from django.contrib import admin
from product.models import Product
# Register your models here.
@admin.register(Product)
class AdminMyUser(admin.ModelAdmin):
    list_display = ['name', 'weight', 'price']