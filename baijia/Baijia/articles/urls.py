from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^frame/$', views.frame, name='frame'),
    url(r'^frame/(?P<author_name>.*)/$', views.auth_frame, name='frame'),
]
