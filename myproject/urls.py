from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('onlinecourse/', include('onlinecourse.urls')),
    path('', include('onlinecourse.urls')),  # Redireciona a URL raiz para o app onlinecourse
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
