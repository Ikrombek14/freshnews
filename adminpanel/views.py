
from .forms import PostForm, YoutubeVideoForm, AdvertisementForm
from news.models import Post, Advertisement, YoutubeVideo
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404




@login_required
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

@login_required
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})

@login_required
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_form.html', {'form': form})

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'post_confirm_delete.html', {'object': post})





@login_required
def youtube_video_list(request):
    """View to display a list of all YouTube videos."""
    videos = YoutubeVideo.objects.all()
    return render(request, 'youtube_video_list.html', {'videos': videos})

@login_required
def youtube_video_detail(request, pk):
    """View to display details of a specific YouTube video."""
    video = get_object_or_404(YoutubeVideo, pk=pk)
    return render(request, 'youtube_video_detail.html', {'video': video})

@login_required
def youtube_video_create(request):
    if request.method == "POST":
        form = YoutubeVideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            video.save()
            return redirect('youtube_video_list')
    else:
        form = YoutubeVideoForm()
    return render(request, 'youtube_video_form.html', {'form': form})

@login_required
def youtube_video_update(request, pk):
    video = get_object_or_404(YoutubeVideo, pk=pk)
    if request.method == "POST":
        form = YoutubeVideoForm(request.POST, instance=video)
        if form.is_valid():
            form.save()
            return redirect('youtube_video_detail', pk=pk)
    else:
        form = YoutubeVideoForm(instance=video)
    return render(request, 'youtube_video_form.html', {'form': form})

@login_required
def youtube_video_delete(request, pk):
    video = get_object_or_404(YoutubeVideo, pk=pk)
    if request.method == "POST":
        video.delete()
        return redirect('youtube_video_list')
    return render(request, 'youtube_video_confirm_delete.html', {'object': video})




@login_required
def advertisement_list(request):
    advertisements = Advertisement.objects.all()
    return render(request, 'advertisement_list.html', {'advertisements': advertisements})

@login_required
def advertisement_detail(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    return render(request, 'advertisement_detail.html', {'advertisement': advertisement})

@login_required
def advertisement_create(request):
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.save()
            return redirect('advertisement_list')
    else:
        form = AdvertisementForm()
    return render(request, 'advertisement_form.html', {'form': form})

@login_required
def advertisement_update(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.method == "POST":
        form = AdvertisementForm(request.POST, request.FILES, instance=advertisement)
        if form.is_valid():
            form.save()
            return redirect('advertisement_detail', pk=pk)
    else:
        form = AdvertisementForm(instance=advertisement)
    return render(request, 'advertisement_form.html', {'form': form})

@login_required
def advertisement_delete(request, pk):
    advertisement = get_object_or_404(Advertisement, pk=pk)
    if request.method == "POST":
        advertisement.delete()
        return redirect('advertisement_list')
    return render(request, 'advertisement_confirm_delete.html', {'object': advertisement})



@login_required
def home(request):
    return render(request, 'home.html')

# Login
from django.contrib.auth import  login, logout
from django.contrib.auth.forms import AuthenticationForm

# Login view
def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/TypeError')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def custom_logout(request):
    logout(request)
    return redirect('custom_login')



from django.contrib.auth.decorators import login_required
from .forms import ProfileForm
from .models import Profile

@login_required
def view_profile(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)

    return render(request, 'profile.html', {'profile': profile})

@login_required
def update_profile(request):
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('view_profile')
    else:
        form = ProfileForm(instance=profile)
    return render(request, 'update_profile.html', {'form': form})


