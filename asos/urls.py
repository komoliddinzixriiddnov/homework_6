
from django.contrib import admin
from django.urls import path, include
from .views import LandingPageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("user.urls")),
    path("",LandingPageView.as_view(),name='landing-page'),
]
