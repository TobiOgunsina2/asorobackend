from django.urls import path, include
from . import views
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenObtainPairView
)

urlpatterns = [
    path("user/register/", views.CreateUserView.as_view(), name="register"),
    path('units/', views.UnitList.as_view(), name="unit-list"),
    path('unit/<int:uid>/lesson/<int:lid>/', views.GetLesson.as_view(), name='get-lesson'),
    path('phrase/<int:pk>/', views.GetPhrase.as_view(), name='get-word'),
    path('review/', views.GetReview.as_view(), name='get_token'),
    path('token/', views.MyTokenObtainPairView.as_view(), name='get_token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='refresh'),
    path("progress/", include('progress.urls'))
]