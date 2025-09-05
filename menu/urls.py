from django.urls import path
from .views import (
    DishListAPIView,
    DishDetailAPIView,
    DishCreateAPIView,
    DishUpdateAPIView,
    DishDeleteAPIView,
    RetrieveUpdateDestroyAPIView,
    ReviewListCreateAPIView,
    AddReviewToDishView
)

urlpatterns = [
    path('dishes/', DishListAPIView.as_view(), name='dish-list'),
    path('dishes/<int:pk>/', DishDetailAPIView.as_view(), name='dish_detail'),
    path('dishes/create/', DishCreateAPIView.as_view(), name='dish_create'),
    path('dishes/update/<int:pk>/', DishUpdateAPIView.as_view(), name='dish_update'),
    path('dishes/delete/<int:pk>/', DishDeleteAPIView.as_view(), name='dish_delete'),
    path('dishes/retrieve-update-destroy/<int:pk>/', RetrieveUpdateDestroyAPIView.as_view(), name='dish_retrieve_update_destroy'),
    path('reviews/', ReviewListCreateAPIView.as_view(), name='review-list-create'),
    path('<int:pk>/review/', AddReviewToDishView.as_view(), name='review-create'),
]
