from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from places import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
