from django.urls import path
from .views import main, post_detail, post_by_categories, search
urlpatterns = [
    
    path("", main, name="main"),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('category/<str:category_name>/', post_by_categories, name='post_by_categories'),
    path('search/', search, name='search'),
]