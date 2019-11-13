from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from search import views as src_views
from results import views as res_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', src_views.home, name = "home"),
    path('results/', res_views.result, name = "results"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
