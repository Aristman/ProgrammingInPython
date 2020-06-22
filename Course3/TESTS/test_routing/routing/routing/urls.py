from django.conf.urls import url
from django.urls import path

from routing.views import simple_route

urlpatterns = [
    path('simple_route/', simple_route)
]
