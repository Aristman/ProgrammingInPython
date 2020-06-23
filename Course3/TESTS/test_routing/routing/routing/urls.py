from django.conf.urls import url

import routing.views as rv

urlpatterns = [
    url(r'simple_route/$', rv.simple_route),
    url(r'^slug_route/(?P<slug>[0-9a-z-_]{1,16})/$', rv.slug_route),
    url(r'^sum_route/(?P<a>[-]?\d+)/(?P<b>[-]?\d+)/$', rv.sum_route),
    url(r'sum_get_method/$', rv.sum_get_method),
    url(r'sum_post_method/$', rv.sum_post_method),
]
