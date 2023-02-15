from django.urls import path

from . import views

urlpatterns = [
    path("", views.AllContactsAPIView.as_view()),
    path("<int:pk>/", views.SingleContactsAPIView.as_view()),
    
]
