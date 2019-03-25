from qa.views import test
urlpatterns = patterns('qa.views',
    url(r'^$', test, name='qa'),
    url(r'^login/', test, name='login'),
    url(r'^question/\d\d\d/', test, name='question'),
    url(r'^ask', test, name='ask'),
    url(r'^popular', test, name='popular'),
    url(r'^new/', test, name='new'),
)
