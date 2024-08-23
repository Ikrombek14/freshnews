from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminPanel/', include('adminPanel.urls')),

] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('news.urls')),
<<<<<<< HEAD
    path('adminPanel/', include('adminPanel.urls')),
=======

>>>>>>> 5c11770311be1361b23b495ae7a0a46d060ba299
)





if settings.DEBUG:
    urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



