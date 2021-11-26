import os
import json

from django.shortcuts import render

# Путь к папке текущйего файла
MODULE_DIR = os.path.dirname(__file__)


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    # Путь к файлу goods.json
    file_path = os.path.join(MODULE_DIR, 'fixtures/goods.json')
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'products_categories': ['Новинки', 'Одежда', 'Обувь', 'Аксессуары', 'Подарки'],
        'products': json.load(open(file_path, encoding='utf8'))
    }
    return render(request, 'products/products.html', context)


def test_context(request):
    # context = content, мы формируем контекст (контент) и передаем его в шаблон
    # формируем данные в контроллере и передаем в шаблон
    context = {
        'title': 'GeekShop',
        'header': 'Добро пожаловать на сайт!',
        'user': 'Иван Иванов',
        'products': [
            {'name': 'Худи черного цвета с монограммами adidas Originals', 'price': 6090},
            {'name': 'Синяя куртка The North Face', 'price': 23725},
            {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': 3390},
        ],
        'is_promotion': True,
    }
    return render(request, 'products/test-context.html', context)
