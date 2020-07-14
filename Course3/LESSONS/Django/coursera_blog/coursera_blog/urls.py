"""coursera_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
#from core.views import index

from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
import core.views as core

import blog.views as blog

urlpatterns = [
    re_path(r'topic/(?P<pk>\d+)', core.topic_details, name='topic_details'),
    path('blog/index/', blog.index),
    path('index/', core.index, name='index'),
    path('admin/', admin.site.urls),
    path('form/', include('form1.urls')),
    path('login/', auth_views.LoginView.as_view()),
    path('feedback/', include('feedback.urls')),
]
