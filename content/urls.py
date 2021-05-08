from django.urls import path

from .views import HomePageTemplateView

app_name = "content"

urlpatterns = [
    path("", HomePageTemplateView.as_view(), name="home_page"),
]
