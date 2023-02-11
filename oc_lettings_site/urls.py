from django.contrib import admin
from django.urls import path, include

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings_index')),
    path('profiles/', include('profiles.urls', namespace='profiles_index')),
    path('admin/', admin.site.urls),
]
