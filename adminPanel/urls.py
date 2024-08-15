
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # Post URLs

    path('posts/', views.post_list, name='post_list'),
    path('posts/<int:pk>/', views.post_detail, name='post_detail'),
    path('posts/new/', views.post_create, name='post_create'),
    path('posts/<int:pk>/edit/', views.post_update, name='post_update'),
    path('posts/<int:pk>/delete/', views.post_delete, name='post_delete'),

    # Advertisement URLs
    path('advertisements/', views.advertisement_list, name='advertisement_list'),
    path('advertisements/<int:pk>/', views.advertisement_detail, name='advertisement_detail'),
    path('advertisements/new/', views.advertisement_create, name='advertisement_create'),
    path('advertisements/<int:pk>/edit/', views.advertisement_update, name='advertisement_update'),
    path('advertisements/<int:pk>/delete/', views.advertisement_delete, name='advertisement_delete'),
]
