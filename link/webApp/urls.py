from django.conf.urls import url
from webApp.views import Index

urlpatterns = [
    url(r'^$', Index.as_view(), name='index'),
]