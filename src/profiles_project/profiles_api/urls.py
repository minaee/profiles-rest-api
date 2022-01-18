import imp
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^helloview', views.HelloApiView.as_view()),
    
]