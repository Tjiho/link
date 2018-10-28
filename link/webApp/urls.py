from django.conf.urls import url
from webApp.views import Index,Delete,Url_load

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^delete/(?P<key>\w+)/$', Delete.as_view(), name='delete'),
    url(r'^index.html$', Index.as_view()),
    url(r'^index$', Index.as_view()),
    url(r'^(?P<name>[a-zA-Z]+)$', Url_load.as_view(), name='Url_load'),

]