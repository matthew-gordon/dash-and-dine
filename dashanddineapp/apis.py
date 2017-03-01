from django.http import JsonResponse

from dashanddineapp.models import Restaurant
from dashanddineapp.serializers import RestaurantSerializer

def customer_get_restaurant(request):
    restaurants = RestaurantSerializer(
        Restaurant.objects.all().order_by("-id"),
        many = True,
        context = {"request": request}
    ).data

    return JsonResponse({"restaurants": restaurants})
