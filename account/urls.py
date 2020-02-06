from django.urls import path
from .views import AccountJoinView, AccountLoginView

urlpatterns = [
    path('/up', AccountJoinView.as_view()),
    path('/in', AccountLoginView.as_view()),
    ]

