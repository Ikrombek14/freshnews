from django.http import HttpResponseRedirect
from django.urls import path

from . import translation
from .views import main, post_detail, post_by_categories, search
from django.utils.translation import activate

def set_language(request, lang_code):
    activate(lang_code)
    request.session[translation.LANGUAGE_SESSION_KEY] = lang_code
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
urlpatterns = [
    
    path('', main, name="main"),
    path('post/<slug:slug>/', post_detail, name='post_detail'),
    path('category/<str:category_name>/', post_by_categories, name='post_by_categories'),
    path('search/', search, name='search'),
]