from .views import SearchListView

from django.urls import path

urlpatterns = [
    path('/query', SearchListView.as_view())
]
