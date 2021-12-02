from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Index, name='index'),
    path('ev/', include('events.urls')),
    path('ne/', include('news.urls')),
]
