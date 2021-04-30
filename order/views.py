from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import OrderSerializer
from .models import Order

class OrderList(APIView):
    def get(self, request, *args, **kwargs):
        orders = Order.objects.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(data=serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.POST)
        if serializer.is_valid():
            order_object = serializer.save()
            json_serializer = OrderSerializer(instance=order_object)
            return Response(data=json_serializer.data, status=201)
        return Response(data=serializer.errors)


class OrderDetail(APIView):
    def get(self, request, *args, **kwargs):
        order_object = Order.objects.get(pk=kwargs.get('pk'))
        serializer = OrderSerializer(instance=order_object)
        return Response(data=serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs['pk']
        order = Order.objects.get(pk=pk)

        data = request.POST
        serializer = OrderSerializer(data=data)

        if serializer.is_valid():
            order.user = serializer.validated_data.get('user')
            order.dish = serializer.validated_data.get('dish')
            order.address = serializer.validated_data.get('address')
            order.phone = serializer.validated_data.get('phone')
            order.save()
            serialized_object = OrderSerializer(order)
            json_data = serialized_object.data
            return Response(data=json_data)
        return Response(data=serializer.errors)



    def delete(self, request, *args, **kwargs):
        order = Order.objects.get(pk=kwargs.get('pk'))
        order.delete()
        return Response(data={'message': 'Блюдо было удалено'})