from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView

from .models import Dish
from .serializers import DishListSerializer
# Create your views here.
class DishListAPIView(ListAPIView):
    queryset = Dish.objects.order_by('name')
    serializer_class = DishListSerializer
    # def get(self, request, *args, **kwargs):
    #     dishes = Dish.objects.order_by('name')
    #     dishes_serialized = DishListSerializer(dishes, many=True)
    #     return Response(data=dishes_serialized.data)
