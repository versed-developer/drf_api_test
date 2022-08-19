from django.urls import path
from .views import (
   TimeLogCreateAPIView,
   TimeLogListAPIView,
   TimeLogDeleteAPIView,
   TimeLogDetailAPIView,
   TimeLogUpdateAPIView
)

urlpatterns = [
    path('', TimeLogListAPIView.as_view(), name='list'),
    path('create', TimeLogCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', TimeLogDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', TimeLogDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', TimeLogUpdateAPIView.as_view(), name='update')
]
