from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from . models import *

# Register your models here.
@admin.register(Customer)
class CustomerModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','name','locality','division', 'district','zipcode']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','selling_price','discount_price','description', 'brand','category','product_image']

@admin.register(Cart)
class CardModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','product','quantity']

@admin.register(OrderPlaced)
class OrderPlacedModelAdmin(admin.ModelAdmin):
    list_display = ['id','user','customer','product','quantity', 'order_date','status']

