from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
    path('complete/', views.UpdateProgress.as_view(), name='update-progress'),
    path('profile/<int:id>/', views.GetProfile.as_view(), name='get-profile'),
]