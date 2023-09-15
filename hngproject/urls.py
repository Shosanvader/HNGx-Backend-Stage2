from django.contrib import admin
from django.urls import path, include, re_path

urlpatterns = [
    re_path(r'^api/?', include('api.urls')),
    path('admin/', admin.site.urls),
]
