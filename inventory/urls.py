from django.urls import path

from . import views

urlpatterns = [
    path("", views.AllProductsView.as_view()),
    path("c/", views.AllCategoryView.as_view()),
    path("pt/", views.AllProductTypes.as_view()),
    path("c/<str:slug>/", views.SingleCategoryView.as_view()),
    path("sc/", views.AllSubcategoryView.as_view()),
    path("sc/<str:slug>/", views.SingleSubcategoryView.as_view()),
    path("scc/", views.AllLowerSubcategoryView.as_view()),
    path("scc/<str:slug>/", views.SingleLowerSubcategoryView.as_view()),
    path("f/", views.AllFlashsaleView.as_view()),
    path("f/all/", views.AllFlashsaleProductsView.as_view()),
    path("f/disable/", views.DisableFlashsalesView.as_view()),
    path("<str:slug>/", views.SingleProductView.as_view()),
]
