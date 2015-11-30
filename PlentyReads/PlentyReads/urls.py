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
# from django.conf.urls import include, url
# from django.contrib import admin




# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     # url(r'^upload/pdf/', include('mybooks.urls')),
#     url(r'^$', include('mybooks.urls')),
#     url(r'^landingPage/', include('mybooks.urls2')),
#     url(r'^success/', 'mybooks.views.registerSuccess'),
#     # url(r'^uploads/', include('bookstore.urls')),
#     # url(r'^admin/uploads/', include(admin.site.urls)),
# ]
from django.conf.urls import patterns, include, url
from mybooks.views import *
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    # url(r'^$', 'mybooks.views.login'),
    # url(r'^logout/$', logout_page),
    # # url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page

    url(r'^register/$', register),
    # url(r'^register/$', 'mybooks.views.login'),
    url(r'^register/success/$', register_success),
    url(r'^home/$', home),
    
    # url(r'^home/Search.html', include('mybooks.urls')),
    url(r'^home/Search.html', include('mybooks.urls',namespace="Books")),
    url(r'^admin/', include(admin.site.urls)),

    url(r'^home/ReadBook/$', pdf),
    url(r'^home/ReadBook/load/$', load_pdf),
    url(r'^home/ReadBook/show/(?P<id_pdf>.*)', show_pdf),
)