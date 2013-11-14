from rest_framework import generics
from rea.models.contracts import Order
from rea.serializers.contracts import OrderSerializer


class CreateOrderDetail(generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
