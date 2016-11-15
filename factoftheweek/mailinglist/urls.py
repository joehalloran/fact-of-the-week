from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

app_name = 'mailinglist'
urlpatterns = [
    url(r'^join/$', views.Join.as_view(), name='join'),
    url(r'^unsubscribe/(?P<pk>[0-9]+)/$', views.UnsubscribeConfirm.as_view(), name='unsubscribe-confirm'),
    url(r'^unsubscribe/$', views.Unsubscribe.as_view(), name='unsubscribe'),
    url(r'^thanks/$', TemplateView.as_view(template_name='mailinglist/thanks.html'), name='thanks'),
]
