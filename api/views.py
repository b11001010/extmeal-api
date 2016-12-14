import json
from collections import OrderedDict
from django.http import HttpResponse
from django.shortcuts import render
from api.models import Food
# Create your views here.


def food_list(request):
    """食品のリストのJSONを返す"""
    foods = []
    for food in Food.objects.all():

        food_dict = {
            'id': food.id,
            'name': food.name,
            'url': food.url,
            'price': food.price,
            'energy': food.energy,
            'carbohydrates': food.carbohydrates,
            'protein': food.protein,
            'fat': food.fat,
            'calcium': food.calcium,
            'iron': food.iron,
            'vitaminA': food.vitaminA,
            'vitaminB1': food.vitaminB1,
            'vitaminB2': food.vitaminB2,
            'vitaminC': food.vitaminC,
        }

        foods.append(food_dict)
        problems_json = json.dumps(foods, ensure_ascii=False)
    return HttpResponse(problems_json, content_type='application/json')