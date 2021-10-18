from rest_framework import  serializers
from order.models import Shop, Menu, Order, Orderfood

class Shopserializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'

class Menuserializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'