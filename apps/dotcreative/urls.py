from django.urls import path
from apps.dotcreative import views
from apps.dotcreative.views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('blog/', blog_page, name='blog'),
    path('contacts/', contacts, name='contacts'),
]