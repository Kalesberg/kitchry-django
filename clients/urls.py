from django.conf.urls import url

from . import views

app_name = 'clients'
urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^new/$', views.new, name='new'),
	url(r'^(?P<alias>[a-z0-9-]+)/$', views.client, name='client'),
]