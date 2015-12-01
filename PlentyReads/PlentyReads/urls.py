# """PlentyReads URL Configuration

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/1.8/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
# Including another URLconf
#     1. Add an import:  from blog import urls as blog_urls
#     2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
# """

from django.conf.urls import patterns, include, url
from mybooks.views import *
from django.contrib import admin

urlpatterns = patterns('',
    # url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^$', 'mybooks.views.login'),
    url(r'^logout/$', logout_page),
    
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    
    
    # url(r'^home/Search.html', include('mybooks.urls')),
    url(r'^home/search/', include('mybooks.urls',namespace="Books")),
    url(r'^home/search/index.html(?P<key>.*)',include('mybooks.urls2',namespace="Books")),
    url(r'^home/(?P<id_user>.*)', home),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ReadBook/$', pdf),
    url(r'^ReadBook/load/$', load_pdf),
    url(r'^ReadBook/show/(?P<id_pdf>.*)', show_pdf),
    url(r'^ReadBook/$', pdf),
    url(r'^load/$', load_pdf),
    url(r'^show/(?P<id_pdf>.*)', show_pdf),

    url(r'^profile/$', profile),

)