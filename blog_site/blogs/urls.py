from django.conf.urls import url

from .views import index
urlpatterns = [
    url(r'^article/(?P<articleNum>[0-9])/$', index),
]
