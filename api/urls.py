from django.urls import path
from .views import *

urlpatterns = [
    path('create/',AditCreate.as_view(),name='create'),
    path('update/<int:pk>/',AditUpdate.as_view(),name='update'),
    path('delete/<int:pk>/',AditDestroy.as_view(),name='delete'),
    path('ret/<int:pk>/',AditRetireve.as_view(),name='ret'),
    path('alc/',AditListCreate.as_view(),name='alc'),
    path('rav/<int:pk>/',AditRAV.as_view(),name='rav'),
    path('av/',AditAV.as_view(),name='av'),
    path('lav/',AditLAV.as_view(),name='lav'),
    path('rudav/<int:pk>/',AditRUDAV.as_view(),name='rudav'),
    path('rdav/<int:pk>/',AditRDAV.as_view(),name='rdav'),
    path('ruav/<int:pk>/',AditRUAV.as_view(),name='ruav'),
]