from django.urls import path
from . import views

urlpatterns = {
    path('', views.custom_login, name='custom_login'),
    path('logout/', views.custom_logout, name='logout'),
    path('profile/', views.view_profile, name='view_profile'),
    path('profile/update/', views.update_profile, name='update_profile'),

    path('home/', views.home, name='home'),
    # Post URLs
    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/create/', views.post_create, name='post_create'),
    path('posts/<int:pk>/update/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # YoutubeVideo URLs
    path('videos/', views.youtube_video_list, name='youtube_video_list'),
    path('videos/<int:pk>/', views.youtube_video_detail, name='youtube_video_detail'),
    path('videos/create/', views.youtube_video_create, name='youtube_video_create'),
    path('videos/<int:pk>/update/', views.youtube_video_update, name='youtube_video_update'),
    path('videos/<int:pk>/delete/', views.youtube_video_delete, name='youtube_video_delete'),

    # Advertisement URLs
    path('advertisements/', views.advertisement_list, name='advertisement_list'),
    path('advertisements/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('advertisements/create/', views.advertisement_create, name='advertisement_create'),
    path('advertisements/<int:pk>/update/', views.advertisement_update, name='advertisement_update'),
    path('advertisements/<int:pk>/delete/', views.advertisement_delete, name='advertisement_delete'),
}
