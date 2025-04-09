from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Product
from .models import Category
from .models import Comment

admin.site.register(Product)
admin.site.register(Comment)


def site():
    return None


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'parent', 'created_at')
    prepopulated_fields = {'slug': ('name',)}
