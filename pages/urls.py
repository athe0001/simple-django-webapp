from django.urls import path

from .views import HelloWorldPageView

urlpatterns = [
    path('', HelloWorldPageView.as_view(), name = 'hello world')
]
