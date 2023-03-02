from django.urls import path
from apps.single_services import views
from apps.single_services.views import *


urlpatterns = [
    path('single_serv1/', single_service1, name='single_serv1'),
    path('single_serv2/', single_service2, name='single_serv2'),
]
