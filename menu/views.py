from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Dish, Review
from .serializers import DishSerializer, DishDetailSerializer, ReviewSerializer
from .filters import DishFilters


class DishListAPIView(generics.ListAPIView):
    queryset = Dish.objects.filter(is_available=True)
    serializer_class = DishSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filterset_class = DishFilters
    ordering_fields = ['price', 'weight']
    search_fields = ['name']


class DishDetailAPIView(generics.RetrieveAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishDetailSerializer


class DishCreateAPIView(generics.CreateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishUpdateAPIView(generics.UpdateAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class DishDeleteAPIView(generics.DestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class RetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer


class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all().order_by('-created_at')
    serializer_class = ReviewSerializer


class AddReviewToDishView(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def post(self, request, pk, *args, **kwargs):
        dish = get_object_or_404(Dish, pk=pk)
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(dish=dish)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


