from django.conf.urls import url
from . import views


from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm

urlpatterns = [
    url('^register/', CreateView.as_view(
            template_name='auth/register.html',
            form_class=UserCreationForm,
            success_url='/'
    )),
    # url('^accounts/', include('django.contrib.auth.urls')),
    url(r'^$', views.SearchView.as_view(), name='search'),
    # url(r'^$',  'mybooks.views.RegisterView'),
    # url(r'^(?P<pk>[0-9]+)/ /$',  views.LandingView.as_view(), name='landingPage'),

    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

     # url(r'^$', views.UploadView.as_view(), name='upload'),

]