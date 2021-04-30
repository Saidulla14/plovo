from django.urls import path
from .views import OrderList, OrderDetail

urlpatterns = [
    path('', OrderList.as_view(), name='order-list-create'),
    path('<int:pk>/', OrderDetail.as_view(), name='order'),
]