from django.conf.urls import url
from qa.views import test, question

urlpatterns = [
    url(r'^(?P<num>\d+)/$', question),
]
