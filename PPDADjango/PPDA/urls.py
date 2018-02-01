from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^uploadData/$', views.myFormView, name='myFormView'),
]
