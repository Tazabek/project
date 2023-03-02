from django.urls import path
from apps.services import views
from apps.services.views import *

urlpatterns = [
    path('service1/', service1, name='service1'),
    path('service2/', service2, name='service2'),
    path('service3/', service3, name='service3'),
    path('service4/', service4, name='service4'),
    path('service5/', service5, name='service5'),
]
