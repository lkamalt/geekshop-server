from django.db import models


class ProductCategory(models.Model):
    # uuid = models.UUIDField(primary_key=True)
    # max_length - количество символов
    name = models.CharField(max_length=64, unique=True)
    # Данное поле может быть пустым
    description = models.TextField(blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=256)
    # Класс, который хранит в себе путь до картинки или файла (FileField)
    # products_images - папка
    image = models.ImageField(upload_to='products_images', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    # max_digits - максимальное количество цифр до запятой
    # decimal_places - сколько цифр после запятой
    # default есть во всех классах
    # Если не указан default и нет blank=True, null=True, то это поле обязательно для заполнения
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(default=0)
    # Задаем внешний ключ, oneToMany и каскадное удаление при удалении категории
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
