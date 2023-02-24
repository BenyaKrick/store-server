from django.contrib import admin
from .models import ProductCategory, Product, ProductCategoryNew
admin.site.register(Product)
admin.site.register(ProductCategoryNew)
admin.site.register(ProductCategory)
