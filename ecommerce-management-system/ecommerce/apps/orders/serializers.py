from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'quantity', 'price']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price', 'created_at', 'updated_at']

    def create(self, validated_data):
        items_data = validated_data.pop('items')
        order = Order.objects.create(**validated_data)
        for item_data in items_data:
            OrderItem.objects.create(order=order, **item_data)
        return order

    def update(self, instance, validated_data):
        items_data = validated_data.pop('items', None)
        instance.user = validated_data.get('user', instance.user)
        instance.total_price = validated_data.get('total_price', instance.total_price)
        instance.save()

        if items_data:
            instance.items.all().delete()  # Clear existing items
            for item_data in items_data:
                OrderItem.objects.create(order=instance, **item_data)

        return instance