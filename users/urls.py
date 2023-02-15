from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserListAPIView.as_view()),
    path("register/", views.CreateUserAPIView.as_view(), name="register"),
    path("login/", views.LoginUserAPIView.as_view(), name="login"),
    path("verify/", views.VerifyUserAPIView.as_view()),
    path("update/<int:pk>/", views.UpdateUserAPIView),
    path("<int:pk>/change-password/", views.ChangePasswordAPIView),
    path("<int:id>/", views.UserDetailAPIView.as_view()),
    # path("delete/<str:id>/", views.DeleteUserAPIView.as_view()),
]
