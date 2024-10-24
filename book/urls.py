from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from shops import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('musicshop.urls', namespace='shops')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)