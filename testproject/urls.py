from django.contrib import admin
from django.urls import path, include


from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("testapp.urls")),
    path('settings', include("app2.urls"))
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

#install Pillow (pip install Pillow)
