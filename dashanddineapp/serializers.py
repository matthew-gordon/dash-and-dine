from rest_framework import serializers

from dashanddineapp.models import Restaurant

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ("id", "name", "phone", "address", "logo")
