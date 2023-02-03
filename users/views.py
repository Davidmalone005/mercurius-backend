from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import APIView, api_view
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.request import Request
from rest_framework.response import Response

from .models import User
from .serializers import (
    ChangePasswordSerializer,
    CreateUserSerializer,
    UpdateUserSerializer,
    VerifyUserSerializer,
)


class CreateUserAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def create(self, request: Request):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid():
            serializer.save()

            response = {
                "message": "User Created Successfully",
                "user_data": serializer.data,
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(
            data=serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE
        )


class LoginUserAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer

    def post(self, request: Request):
        email = request.data.get("email")
        password = request.data.get("password")

        user = authenticate(email=email, password=password)

        if user is not None:
            if Token.objects.filter(user=user).exists():
                response = {
                    "success": "Login Successful",
                    "token": user.auth_token.key,
                }
                return Response(data=response, status=status.HTTP_200_OK)
            else:
                return Response(
                    data={
                        "error": "Admin User is not allowed to login here. Use the backend."
                    },
                    status=status.HTTP_406_NOT_ACCEPTABLE,
                )

        return Response(
            data={"error": "Invalid email or password"},
            status=status.HTTP_408_REQUEST_TIMEOUT,
        )

    def get(self, request: Request):
        content = {"user": str(request.user), "auth": str(request.auth)}

        return Response(data=content, status=status.HTTP_200_OK)


class VerifyUserAPIView(generics.GenericAPIView):
    queryset = User.objects.all()
    serializer_class = VerifyUserSerializer

    def post(self, request: Request):
        email = request.data.get("email")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                data={"error": "User Not Found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if user:
            response = {
                "id": user.id,
                "fullname": user.fullname,
                "email": user.email,
                "phone": user.phone,
                "gender": user.gender,
                "dob": user.dob,
            }

            return Response(data=response, status=status.HTTP_200_OK)


# class DeleteUserAPIView(generics.DestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = CreateUserSerializer
#     lookup_field = "id"
#     # permission_classes = [permissions.IsAdminUser]

#     def delete(self, request, *args, **kwargs):
#         print("Onimisea's token ", request.user)

#         return self.destroy(request, *args, **kwargs)

#     Response(
#         {"message": "User Deleted Successfully"}, status=status.HTTP_201_CREATED
#     )


class UserListAPIView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UserDetailAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    lookup_field = "id"


# class UpdateUserAPIView(APIView):
#     queryset = User.objects.all()
#     serializer_class = UpdateUserSerializer

#     def put(self, request, *args, **kwargs):
#         user_email = request.GET['email']
#         # user_email = self.serializer_class(instance=User, data=request.data)
#         user = User.objects.get(email=user_email)
#         user_data = self.serializer_class(instance=user)
#         print(user_email)

#         return Response(status=status.HTTP_200_OK)
# data = self.serializer_class(instance=user, data=request.data)

# print(request.data)
# if data.is_valid():
#     data.save()
#     response = {
#         "message": "Account Updated Successfully",
#         "account_info": data.data,
#     }

#     return Response(data=response, status=status.HTTP_200_OK)
# else:
#     response = {
#         "error": "Account Update Failed. Try Again Later",
#     }
#     return Response(data=response, status=status.HTTP_406_NOT_ACCEPTABLE)


@api_view(http_method_names=["PUT"])
def UpdateUserAPIView(request: Request, pk):
    permission_classes = (IsAuthenticated,)
    user = get_object_or_404(User, pk=pk)
    data = request.data
    serializer = UpdateUserSerializer(instance=user, data=data)

    if serializer.is_valid():
        serializer.save()

        response = {
            "success": "Account Updated Successfully",
            "data": serializer.data,
        }

        return Response(data=response, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(http_method_names=["PUT"])
def ChangePasswordAPIView(request: Request, pk):
    user = get_object_or_404(User, pk=pk)
    data = request.data
    serializer = ChangePasswordSerializer(instance=user, data=data)
    permission_classes = (IsAuthenticated,)
    # print(request.user)

    if serializer.is_valid():
        serializer.save()

        response = {
            "success": "Password Changed Successfully",
            "data": serializer.data,
        }

        return Response(data=response, status=status.HTTP_200_OK)

    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
