from django import forms
from news.models import Post, Advertisement, YoutubeVideo

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'slug', 'category', 'image', 'video']

class YoutubeVideoForm(forms.ModelForm):
    class Meta:
        model = YoutubeVideo
        fields = ['title', 'category', 'content', 'youtube_url', 'slug']

class AdvertisementForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = ['title', 'image', 'url', 'is_active']



#profile
from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']
