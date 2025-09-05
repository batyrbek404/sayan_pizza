from django.urls import path
from .views import LoginView, RegisterView, LogoutView, ProfileView, FeedbackSendView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('me/', ProfileView.as_view(), name='profile'),
    path('feedback/',FeedbackSendView.as_view(), name='feedback')
]
