from django.urls import path
from .api import *

urlpatterns = [
    path('accounts/register/', CreateUserView.as_view(), name='register'),
    path('accounts/login/', LoginUserView.as_view(), name='login'),
    path('accounts/logout/', LogoutUserView.as_view(), name='logout'),

    path('questions/create/', CreateQuestionView.as_view()),
    path('questions/current/get/', GetCurrentUserQuestions.as_view()),
]
