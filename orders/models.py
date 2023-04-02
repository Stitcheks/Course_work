from django.contrib.auth.models import User
from django.db import models
from main.models import Packing


class Contact(models.Model):
    name = models.CharField(verbose_name='Имя', max_length=50)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=13, unique=True)
    processed = models.BooleanField(verbose_name='Обработано', default=False)
    data_added = models.DateTimeField(verbose_name='Дата заявки', auto_now_add=True)

    def __str__(self):
        return f'{self.name}----{self.phone_number}'

    class Meta:
        verbose_name = 'Заявка на обратный звонок'
        verbose_name_plural = 'Заявки на обратный звонок'
        ordering = ('data_added',)


class Order(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='orders',
                                verbose_name='Заказы')
    first_name = models.CharField(verbose_name='Имя', max_length=50)
    last_name = models.CharField(verbose_name='Фамилия', max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=13)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(verbose_name='Оплачено', default=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created',)

    def __str__(self):
        if not self.paid:
            return f'{self.first_name} {self.last_name} {self.phone_number} --- не оплачено'
        else:
            return f'{self.first_name} {self.last_name} {self.phone_number} --- оплачено'

    def get_total_cost(self):
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    packing = models.ForeignKey(Packing, related_name='order_items', verbose_name='товары',
                                default=None, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='цена')
    quantity = models.PositiveIntegerField(default=1, verbose_name='количество')

    def __str__(self):
        return '{}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity
