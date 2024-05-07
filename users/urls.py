from django.urls import path, include
from .views import (
    RegisterView,
    ProfileRetrieveUpdateView,
)


urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('register/', RegisterView.as_view()),
    path('profile/<int:pk>/', ProfileRetrieveUpdateView.as_view()),
]
