from django.shortcuts import render
from .models import ShopDish, ShopRate, ShopLocation, ShopDetails
from pymongo import MongoClient

client = MongoClient('localhost:27017')
db = client.dishs
shop_data = db.dish.find()


def home(request):
    if request.method == 'POST':
        food_search = request.POST.get('food_search').lower()
        food_result = ShopDish.objects.filter(food__contains=food_search).values()
        if food_result:
            shop_details = ShopDetails.objects.all()
            return render(request, 'foodsearch_result.html',
                          {'action': 'Result', 'shop_details': shop_details, 'food_result': food_result})
        else:
            return render(request, 'foodsearch_result.html', {'action': 'NoResult'})

    return render(request, 'index_food_search.html')


def home_restaurant(request):
    if request.method == 'POST':
        restaurant_search = request.POST.get('restaurant_search').lower()
        shop_details= ShopDetails.objects.filter(name__contains=restaurant_search).values()
        if shop_details:
            shop_rate = ShopRate.objects.all()
            return render(request, 'restaurant_search_result.html',
                          {'action': 'Result', 'shop_details': shop_details, 'shop_rate': shop_rate})

        else:
            print("no data")

        print(restaurant_search)

    return render(request, 'index_restaurant_search.html')

