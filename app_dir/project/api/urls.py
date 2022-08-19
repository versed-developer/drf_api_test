from django.urls import path
from .views import (
   ProjectCreateAPIView,
   ProjectListAPIView,
   ProjectDeleteAPIView,
   ProjectDetailAPIView,
   ProjectUpdateAPIView
)

urlpatterns = [
    path('', ProjectListAPIView.as_view(), name='list'),
    path('create', ProjectCreateAPIView.as_view(), name='create'),
    path('delete/<int:pk>/', ProjectDeleteAPIView.as_view(), name='delete'),
    path('detail/<int:pk>/', ProjectDetailAPIView.as_view(), name='detail'),
    path('update/<int:pk>/', ProjectUpdateAPIView.as_view(), name='update')
]
