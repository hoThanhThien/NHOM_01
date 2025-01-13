from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'TRANG QUAN LY'
admin.site.site_title = 'Trang quan ly'
admin.site.index_title = 'Home'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_home.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)