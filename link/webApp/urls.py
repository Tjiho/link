from django.conf.urls import url
from webApp.views import Index
from webApp.views import Delete

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
    url(r'^delete/(?P<key>\w+)/$', Delete.as_view(), name='delete'),
]