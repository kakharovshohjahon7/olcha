from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product
from .models import Category

admin.site.register(Product)


def site():
    return None


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
