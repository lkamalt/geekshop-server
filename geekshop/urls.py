"""geekshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# media 2/3
from django.conf.urls.static import static
# Более правильный спсоб импорта файла settings в Django
from django.conf import settings

from products.views import index, test_context

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('products/', include('products.urls', namespace='products')),
    path('test-context/', test_context, name='test-context')
]

# Если settings.DEBUG = True, значит работаем локально
# media 3/3
if settings.DEBUG:
    # Включаем работу с медиафайлами
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
