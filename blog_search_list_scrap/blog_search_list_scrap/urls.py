from django.urls import path, include

urlpatterns = [
    path('search-list', include('search_list.urls')),
]
