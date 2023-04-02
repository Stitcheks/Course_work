from django.db import models
from django.urls import reverse


class Product(models.Model):
    name = models.CharField(verbose_name='Название продукта', max_length=255)
    availability = models.BooleanField(verbose_name='В наличии', default=True)
    image = models.ImageField(verbose_name='Фотография', upload_to='product')
    catalog = models.ForeignKey('Catalog', on_delete=models.CASCADE)
    brand = models.ForeignKey('Brand', on_delete=models.CASCADE)
    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE)
    clarification = models.ForeignKey('Clarification', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продкуты'
        ordering = ('name',)

    def get_absolute_url(self):
        return reverse(viewname='product_detail', kwargs={'pk': self.pk})


class Packing(models.Model):
    name = models.IntegerField(verbose_name='количество')
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE)
    price = models.DecimalField(verbose_name='цена', max_digits=10, decimal_places=2)
    product = models.ForeignKey('Product', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} {self.unit} --- {self.price} BYN --- {self.product}'

    class Meta:
        verbose_name = 'Вариант фасовки'
        verbose_name_plural = 'Варианты фасовки'
        ordering = ('price',)


class Catalog(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(verbose_name='Фотография', upload_to='category')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Каталог'
        verbose_name_plural = 'Каталоги'
        ordering = ('id',)


class Unit(models.Model):
    name = models.CharField(verbose_name='Единица измерения', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'
        ordering = ('name',)


class Brand(models.Model):
    name = models.CharField(verbose_name='Название бренда', max_length=255)
    image = models.ImageField(verbose_name='Логотип', upload_to='brand')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Бренд'
        verbose_name_plural = 'Бренды'
        ordering = ('name',)


class ProductType(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    catalog = models.ForeignKey('Catalog', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} --- {self.catalog}'

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'
        ordering = ('name',)


class Clarification(models.Model):
    name = models.CharField(verbose_name='Уточнение типа товара', max_length=255)
    product_type = models.ForeignKey('ProductType', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} --- {self.product_type}'

    class Meta:
        verbose_name = 'Уточнение'
        verbose_name_plural = 'Уточнения'
        ordering = ('name',)
