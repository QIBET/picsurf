from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.pictorial,name='pictorial'),
]