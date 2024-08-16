from django.shortcuts import render, get_object_or_404
from .models import Categories, Post, YoutubeVideo
from django.utils import timezone
from django.core.paginator import Paginator
from datetime import timedelta
from django.db.models import Q





def main(request):
    categories = Categories.objects.all()
    all_posts = Post.objects.filter(image__isnull=False).order_by('-created_ad')[:30]
    latest_post_with_image = next((post for post in all_posts if post.image), None)

    latest_posts = {}
    for category in categories:
        latest_post = Post.objects.filter(category=category).order_by('-created_ad').first()
        if latest_post:
            latest_posts[category.name] = latest_post
    print(latest_posts)


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
    jamiyat_posts = Post.objects.filter(category__name='Jamiyat').order_by('-created_ad')[:10]

    sport_posts = Post.objects.filter(category__name='Sport').order_by('-created_ad')[:10]

    now = timezone.now()
    last_week = now - timedelta(days=7)

    weekly_top_posts = Post.objects.filter(created_ad__gte=last_week).order_by('-created_ad')[:7]

    video_posts = YoutubeVideo.objects.filter(youtube_url__isnull=False).order_by('-created_ad')
   






    context = {
        'categories':categories,
        'latest_posts': latest_posts,
        'latest_sport_post':latest_sport_post,
        'latest_post_with_image':latest_post_with_image,
        'latest_jamiyat_post':latest_jamiyat_post,
        'latest_jahon_post':latest_jahon_post,
        'latest_fantexnika_post':latest_fantexnika_post,
        'latest_madaniyat_post':latest_madaniyat_post,

        'post_jamiyat':post_jamiyat,
        'post_sport':post_sport,
        'post_jahon':post_jahon,

        'latest_posts':latest_posts,
        'latest_post':latest_post,
        'jamiyat_posts':jamiyat_posts,
        'sport_posts':sport_posts,
        

        'all_posts':all_posts,
        'weekly_top_posts':weekly_top_posts,
        'video_posts':video_posts,
    }


    return render(request, 'index.html', context)
    
def post_by_categories(request, category_name):
    categories = Categories.objects.all()
    category = get_object_or_404(Categories, name = category_name)
    posts = Post.objects.filter(category=category)
    paginator = Paginator(posts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {
        'categories':categories,
    

        'page_obj':page_obj
    }
    return render(request, 'category.html', context=context)


def post_detail(request, slug):
    categories = Categories.objects.all()
    
    youtube_videos = YoutubeVideo.objects.all().order_by('-created_ad')[:5]
    post = get_object_or_404(Post, slug=slug)
    
    related_posts = Post.objects.filter(category = post.category).exclude(id=post.id)[:5]

    context = {
        'post':post,
        'categories':categories,
        
        'related_posts':related_posts,
        'youtube_videos':youtube_videos
    }
    return render (request, 'details.html', context=context)



def search(request):
    query = request.GET.get('q')
    results = []
    if query:
        results = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)
        )
    return render(request, 'search_results.html', {'results': results, 'query': query})