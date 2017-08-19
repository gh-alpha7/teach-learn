from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.answe,name='answe'),
    ]

