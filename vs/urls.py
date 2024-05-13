from django.urls import path,include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts',create_view, basename="post")
urlpatterns = [
    path('', include(router.urls)),
    # http://127.0.0.1:8000/api/posts/1 this will get all routeres register and if you dont give it number it will take you create and read if you give a number than you can update or delete it as well
     
]