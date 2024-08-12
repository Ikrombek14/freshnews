from django.contrib import admin
from .models import Categories, Post, Advertisement

admin.site.register(Categories)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_ad')

@admin.register(Advertisement)
class Advertisement(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')

# Register your models here.
