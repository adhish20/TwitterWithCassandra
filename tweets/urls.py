from django.conf.urls import patterns, url, include

urlpatterns = patterns('tweets.views',
    url(r'^/?$', 'timeline', name='timeline'),
    url(r'^public/$', 'publicline', name='publicline'),
    url(r'^(?P<username>\w+)/$', 'userline', name='userline'),
)