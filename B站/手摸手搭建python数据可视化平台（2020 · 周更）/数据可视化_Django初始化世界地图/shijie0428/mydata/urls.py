from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^data_demo', views.data_demo),
    url(r'^test', views.test),


]
