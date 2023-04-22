from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile/', ProfileView.as_view(), name='pofile'),
    path('questions/create/', CreateQuestionView.as_view(), name='create-question'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/register/', RegisterView.as_view(), name='register'),
]
