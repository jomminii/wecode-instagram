
from django.urls import path
from .views import CommentView

urlpatterns = [
    path('input', CommentView.as_view()),

]

