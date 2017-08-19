"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('blog.main')),
    url(r'^top/',include('blog.top')),
    url(r'^questions/',include('blog.urls')),
    url(r'^questions/ask/',include('blog.ask')),
    url(r'^questions/ans/',include('blog.an')),
    url(r'^questions/ans/an/',include('blog.ans')),
    url(r'^questions/ans/home/',include('blog.home')),
    
]
