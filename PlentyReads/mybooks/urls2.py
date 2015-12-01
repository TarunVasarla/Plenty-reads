from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.KeySearchView.as_view(), name='keysearch'),

]