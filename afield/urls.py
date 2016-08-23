from django.conf.urls import url
from . import views

app_name = 'afield'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<room_id>[0-9]+)/$', views.index, name='index'),
    url(r'^(?P<room_id>[0-9]+)/(?P<previous_room_action_id>[0-9]+)/$', views.index, name='index'),
]
