from django.urls import path

from . import views

urlpatterns = [
    path("<str:pk>/", views.AllInboxAPIView),
    path("<str:pk>/<str:pk2>/", views.SingleInboxAPIView),
    
]
