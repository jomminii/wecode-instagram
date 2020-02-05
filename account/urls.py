from django.urls import path
from .views import AccountJoinView, AccountLoginView

urlpatterns = [
    path('sign-up', AccountJoinView.as_view()),
    path('sign-in', AccountLoginView.as_view()),
    ]

