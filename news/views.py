from django.shortcuts import render
from .models import Categories, Post
import requests

def main(request):
    categories = Categories.objects.all()

    latest_sport_post = Post.objects.filter(category__name='Sport').order_by('-created_ad').first()
    latest_jamiyat_post = Post.objects.filter(category__name="Jamiyat").order_by('-created_ad').first()
    latest_jahon_post = Post.objects.filter(category__name="Jahon").order_by('-created_ad').first()
    latest_fantexnika_post = Post.objects.filter(category__name="Fan-texnika").order_by('-created_ad').first()
    latest_madaniyat_post =Post.objects.filter(category__name="Shou-biznes").order_by('-created_ad').first()

    post_jamiyat = Post.objects.filter(category__name='Jamiyat').order_by('-created_ad')[1]
    post_sport = Post.objects.filter(category__name='Sport').order_by('created_ad')[1]
    post_jahon = Post.objects.filter(category__name='Jahon').order_by('-created_ad')[1]

    latest_post = Post.objects.latest('created_ad')
    latest_posts = Post.objects.order_by('-created_ad')[:3]#qaynoq yangiliklar uchun 3 ta Post

    jamiyat_posts = Post.objects.filter(category__name='Jamiyat').order_by('-created_ad')[:4]

    context = {
        'categories':categories,
        'latest_sport_post':latest_sport_post,
        'latest_jamiyat_post':latest_jamiyat_post,
        'latest_jahon_post':latest_jahon_post,
        'latest_fantexnika_post':latest_fantexnika_post,
        'latest_madaniyat_post':latest_madaniyat_post,

        'post_jamiyat':post_jamiyat,
        'post_sport':post_sport,
        'post_jahon':post_jahon,

        'latest_posts':latest_posts,
        'latest_post':latest_post,

        'jamiyat_posts':jamiyat_posts

    }


    # You can pass context variables here if needed
    return render(request, 'index.html', context)


