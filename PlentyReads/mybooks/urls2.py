from django.conf.urls import url
from . import views
urlpatterns = [
   url(r'^$', views.LandingView.as_view(), name='landingPage'),

]