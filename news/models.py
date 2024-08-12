from django.db import models
from django.utils.safestring import mark_safe
# Create your models here.


class Categories(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    created_ad = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)

    def get_youtube_embed_url(self):
        if self.youtube_url:
            video_id = self.youtube_url.split('v=')[-1]
            return f"https://www.youtube.com/embed/{video_id}"
        return None

    def youtube_video(self):
        embed_url = self.get_youtube_embed_url()
        if embed_url:
            return mark_safe(
                f'<iframe width="560" height="315" src="{embed_url}" frameborder="0" allowfullscreen></iframe>')
        return None


    def __str__(self):
        return self.title


class Advertisement(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='ads/', blank=True, null=True)
    url = models.URLField()
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



