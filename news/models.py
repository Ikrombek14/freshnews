from django.db import models
from django.urls import reverse
import re

class Categories(models.Model):
    name_uz = models.CharField(max_length=25)
    name_ru = models.CharField(max_length=25)
    name_en = models.CharField(max_length=25)

    def __str__(self):
        # Bu yerda siz istalgan tilni qaytarishingiz mumkin
        return self.name_uz

class Post(models.Model):
    title_uz = models.CharField(max_length=250)
    title_ru = models.CharField(max_length=250)
    title_en = models.CharField(max_length=250)
    content_uz = models.TextField()
    content_ru = models.TextField()
    content_en = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255, null=False)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.title_uz

class YoutubeVideo(models.Model):
    title_uz = models.CharField(max_length=250)
    title_ru = models.CharField(max_length=250)
    title_en = models.CharField(max_length=250)
    content_uz = models.TextField()
    content_ru = models.TextField()
    content_en = models.TextField()
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    youtube_url = models.URLField(blank=True, null=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255, null=False)

    def __str__(self):
        return self.title_uz

    @property
    def embed_url(self):
        if self.youtube_url:
            match = re.search(
                r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:embed\/|v\/|watch\?v=)|youtu\.be\/)([^"&?\/\s]{11})',
                self.youtube_url
            )
            if match:
                video_id = match.group(1)
                return f'https://www.youtube.com/embed/{video_id}'
        return ''

class Advertisement(models.Model):
    title_uz = models.CharField(max_length=200)
    title_ru = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    url = models.URLField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title_uz
