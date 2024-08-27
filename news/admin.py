from django.contrib import admin
from .models import Categories, Post, Advertisement, YoutubeVideo

admin.site.register(Categories)

@admin.register(YoutubeVideo)
class YoutubeVideoAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'category', 'created_ad', 'slug')
    search_fields = ('title_uz', 'content_uz')
    prepopulated_fields = {'slug': ('title_uz',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'category', 'created_ad', 'slug')
    search_fields = ('title_uz', 'content_uz')
    prepopulated_fields = {'slug': ('title_uz',)}

@admin.register(Advertisement)
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ('title_uz', 'is_active', 'created_at')
