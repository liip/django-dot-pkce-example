from django.urls import path
from .views import TestView
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('test/', login_required(TestView.as_view()))
]
