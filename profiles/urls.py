from django.urls import path
from profiles import views

urlpatterns = [
    path('', views.ProfilesList.as_view()),
    path('<int:pk>/', views.ProfileDetail.as_view())
]
