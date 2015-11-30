"""PlentyReads URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mybooks.views import *


urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),
    # url(r'^upload/pdf/', include('mybooks.urls')),
    url(r'^mybooks/', include('mybooks.urls')),
    url(r'^$', 'mybooks.views.index'),
    url(r'^register/$', register),
    
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    # url(r'^uploads/', include('bookstore.urls')),
    # url(r'^admin/uploads/', include(admin.site.urls)),
]