from django.urls import path
from Users.views import ProfileUpdateView

urlpatterns = [
    path('update/<pk>/', ProfileUpdateView.as_view(), name=('profile_update')),
]