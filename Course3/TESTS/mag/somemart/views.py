import json

from django import forms
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views import View

from .models import Item, Review


class FormAddItem(forms.Form):
    title = forms.CharField(max_length=64)
    description = forms.CharField(max_length=1024)
    price = forms.IntegerField(min_value=1, max_value=1000000)


class AddItemView(View):
    """View для создания товара."""
    def get(self,request):
        form = FormAddItem
        return render(request, 'add_item.html', context={'form': form})

    def post(self, request):
        data = {'id': 0}
        form = FormAddItem(request.POST)
        print(form.changed_data)
        try:
            if form.is_valid():
                data['id'] = form.cleaned_data['id']
                return JsonResponse(data, status=201)
            else:
                return HttpResponse('Не все ОК', status=400)
        except:
            pass


class PostReviewView(View):
    """View для создания отзыва о товаре."""

    def post(self, request, item_id):
        # Здесь должен быть ваш код
        return JsonResponse(data, status=201)


class GetItemView(View):
    """View для получения информации о товаре.

    Помимо основной информации выдает последние отзывы о товаре, не более 5
    штук.
    """

    def get(self, request, item_id):
        # Здесь должен быть ваш код
        return JsonResponse(data, status=200)
