from django.urls import path
from .views import TextListCreate

urlpatterns = [
    path('text-docs/', TextListCreate.as_view(), name='text-list-create'),
]