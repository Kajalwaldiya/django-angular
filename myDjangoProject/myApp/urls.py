from django.conf.urls import url, include
from .views import index, detailslist

urlpatterns = [
    url(r'^$', index.as_view(), name='home'),
    url(r'^apiview/$', detailslist.as_view(), name='api')
]
