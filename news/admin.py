from django.contrib import admin
from .models import Categories, Post, Advertisement, YoutubeVideo, FieldTranslation

admin.site.register(Categories)
@admin.register(FieldTranslation)
class FieldTranslationAdmin(admin.ModelAdmin):
    list_display = ('creator_user',)  # Qanday maydonlarni ko'rsatish kerakligi
@admin.register(YoutubeVideo)
class YoutubeVideo(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_ad', 'slug')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_ad', 'slug')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug':('title',)}


@admin.register(Advertisement)
class Advertisement(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')

