from django.conf.urls import url

from .views import PartView


app_name = 'catalog'
urlpatterns = [
    url(r'^parts/(?P<pk>\d+)/$', PartView.as_view(), name='part'),
]
