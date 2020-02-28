from django.urls import path

from .views import HelloWorldPageView, AboutPageView

urlpatterns = [
    path('', HelloWorldPageView.as_view(), name = 'hello world'),
    path('about/', AboutPageView.as_view(), name = "about")
]
