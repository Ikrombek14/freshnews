from django.db import models
from django.urls import reverse

from django.conf import settings
from django.db import models
from parler.models import TranslatableModel, TranslatedFields


class Field(models.Model):
    name = models.CharField(max_length=255)
    # boshqa maydonlar
class FieldTranslation(TranslatableModel):
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    translations = TranslatedFields(
        value=models.CharField(max_length=255)
    )



class Categories(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255, null=False)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('post_detail',
                       args=[self.slug])

    def __str__(self):
        return self.title


import re


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=250)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    content = models.TextField()
    youtube_url = models.URLField(blank=True, null=True)
    created_ad = models.DateTimeField(auto_now_add=True)
    slug = slug = models.SlugField(unique=True, max_length=255, null=False)

    def __str__(self):
        return self.title

    @property
    def embed_url(self):
        if self.youtube_url:
            # Regular expression to extract video ID from various YouTube URL formats
            match = re.search(
                r'(?:https?:\/\/)?(?:www\.)?(?:youtube\.com\/(?:embed\/|v\/|watch\?v=)|youtu\.be\/)([^"&?\/\s]{11})',
                self.youtube_url
            )
            if match:
                video_id = match.group(1)
                return f'https://www.youtube.com/embed/{video_id}'
        return ''


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    url = models.URLField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
