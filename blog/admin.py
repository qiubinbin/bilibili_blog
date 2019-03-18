from django.contrib import admin
from .models import Blog, BlogType


@admin.register(BlogType)  # 注册模板
class BlogTypeAdmin(admin.ModelAdmin):  # Register your models here.
    list_display = ('id', 'type_name')


@admin.register(Blog)  # 注册模板
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'blog_type', 'author', 'create_time', 'last_update')
