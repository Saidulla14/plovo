from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework import mixins
from rest_framework import generics
from rest_framework import status

from django.http import Http404

from .models import Dish
from .serializers import *
# Create your views here.


class DishListAPIView(ListAPIView):
    # queryset = Dish.objects.order_by('name')
    # serializer_class = DishListSerializer


    def get(self, request, *args, **kwargs):
        dishes = Dish.objects.order_by('name')
        dishes_serialized = DishListSerializer(dishes, many=True)
        return Response(data=dishes_serialized.data)


class DishCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        data = request.POST
        serializer = DishCreateSerializer(data=data)
        if serializer.is_valid():
            dish_object = serializer.save()
            return Response(data={'message': 'Блюдо успешно добавлено'})
        return Response(data=serializer.errors)


class DishUpdateAPIView(APIView):
    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        dish = Dish.objects.get(pk=pk)

        data = request.POST
        serializer = DishUpdateSerializer(data=data)

        if serializer.is_valid():
            dish.name = serializer.validated_data.get('name')
            dish.price = serializer.validated_data.get('price')
            dish.save()
            serialized_object = DishSerializer(dish)
            data = serialized_object.data
            return Response(data=data)
        return Response(data=serializer.errors)
class DishDeleteAPIView(APIView):

    def delete(self, request, *args, **kwargs):
        pk = kwargs['pk']
        dish = Dish.objects.get(pk=pk)
        dish.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
class DishDetailAPIView(APIView):
    def get_object(self, pk, *args, **kwargs):
        pk = kwargs['pk']
        dish = Dish.objects.get(pk=pk)
        serializer = DishSerializer(dish, many=True)
        return Response({"dish": serializer.data})