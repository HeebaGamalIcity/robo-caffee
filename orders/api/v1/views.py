from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from orders.models import Order, Product_order
from .serializers import ProductOrderSerializer


def create_qr(order):
    return hex(order.pk)


class OrderView(APIView):

    def get(self, request):
        response_data = {"trigger": 0,
                         "orders": [],
                         "numberOrders": 0}
        try:
            order_queryset = Order.objects.get(qr_code=request.data.get('qrCode'), state=0)
        except:
            return Response(data=response_data, status=status.HTTP_200_OK)

        Product_order_queryset = Product_order.objects.filter(order=order_queryset.pk, state=0)

        product_queryset = []
        for p in Product_order_queryset:
            if p.product.unit.serial_number == int(request.data['unit']):
                product_queryset.append(p)

        if len(product_queryset) != 0:
            response_data["trigger"] = 1

        for p in product_queryset:
            order = {'product':p.product.unit_index,
                     'toppings':[],
                     'toppingsNumber':0,
                     'isImage': False,
                     'image':None}
            if p.topping is not None:
                toppings = p.topping.all()
                for t in toppings:
                    order['toppings'].append(t.unit_index)
                    order['toppingsNumber'] += 1
            if p.image is not None:
                order['isImage'] = True
                order['image'] = p.image.tag
            response_data['orders'].append(order)
            response_data['numberOrders'] += 1
        return Response(data=response_data, status=status.HTTP_200_OK)

    def post(self, request):
        print("order")
        print(request.data)
        print("order")
        order = Order()
        order.save()
        products = request.data.get("order")
        if products is None:
            order.delete()
            return Response(data={
                "state": False,
                "message": "order is null"
            }, status=status.HTTP_400_BAD_REQUEST)
        else:
            for p in products:
                self.create_product_order(order, p)
        order.qr_code = str(create_qr(order))
        order.save()
        return Response(data={
            "state": True,
            "message": "OK",
            "data": str(create_qr(order))},
            status=status.HTTP_200_OK)

    def create_product_order(self, order, product):
        product["order"] = order.pk
        serializer = ProductOrderSerializer(data=product)
        if serializer.is_valid():
            serializer.save()
        else:
            order.delete()
            return Response(data={
                "state": False,
                "message": serializer.errors
            }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def confirm_order(request):
    order_query = Order.objects.get(qr_code=request.data.get('qrCode'))
    print(order_query)
    Product_order_queryset = Product_order.objects.filter(order=order_query.pk)
    order_complete_flag = True
    for p in Product_order_queryset:
        if p.product.unit.serial_number == int(request.data['unit']):
            p.state = 1
            p.save()
        if p.state == 0:
            order_complete_flag = False
        if order_complete_flag:
            order_query.state = 2
            order_query.save()
    return Response(data={"message":1})