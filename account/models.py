from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(verbose_name='Дата рождения', blank=True, null=True)

    def __str__(self):
        return 'Личный кабинет пользователя {}'.format(self.user.username)

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
        ordering = ('id',)
