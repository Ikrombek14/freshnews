from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('dashboard/', include("adminPanel.urls")),
    path('auth/', include("Authenticatet.urls")),

] + i18n_patterns(
    path('i18n/', include('django.conf.urls.i18n')),
    path('', include('news.urls')),
)





if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



def custom_page_not_found_view(request, exception):
    return render(request, '404.html', status=404)


def custom_server_error_view(request):
    return render(request, '500.html', status=500)


handler404 = custom_page_not_found_view
handler500 = custom_server_error_view