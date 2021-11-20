from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'products/index.html')


def products(request):
    return render(request, 'products/products.html')


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
