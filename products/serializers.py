from rest_framework import serializers

from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    final_price = serializers.SerializerMethodField()

    class Meta:
        model = Products
        fields = (
            'id',
            'title',
            'image',
            'price',
            'discount_price',
            'final_price',
            'description',
            'created_at',
            'count',
            'Category',
        )
        read_only_fields = ('id', 'created_at', 'final_price')

    def get_final_price(self, obj):
        return obj.get_final_price()
