
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('builder', include('builder.urls')),
]
if settings.DEBUG == True:
  urlpatterns  += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
