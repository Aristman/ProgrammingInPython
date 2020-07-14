from django.urls import path
from . import views

urlpatterns = [
    path('', views.Form1View.as_view()),
]