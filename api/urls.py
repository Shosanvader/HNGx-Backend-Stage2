from django.urls import path, include, re_path 
from rest_framework.routers import DefaultRouter  
from .views import PersonView  

router = DefaultRouter()  
router.register(r'', PersonView, basename='person') 
urlpatterns = [re_path(r'^/?', include(router.urls))]
