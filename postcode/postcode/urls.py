from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from results import views as res_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', res_views.result, name = "results"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
