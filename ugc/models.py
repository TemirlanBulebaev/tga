from django.db import models

class Profile(models.Model): # Модель для профилей
    external_id = models.PositiveIntegerField(
        verbose_name='ID пользователя',
        unique=True,
    )
    name = models.TextField(verbose_name='Имя пользователя')

    def __str__(self):# Человекочитаемое описание для данного объекта
        return f"#{self.external_id} {self.name}"

    class Meta: # Нужен для добавления метаинформации к нашим моделям
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Message(models.Model):# Модель для сообщений
    profile = models.ForeignKey(
        to='ugc.Profile',
        verbose_name='Профиль',
        on_delete=models.PROTECT,
    )
    text = models.TextField(
        verbose_name='Текст',
    )
    created_at = models.DateTimeField(
        verbose_name='Время получения',
        auto_now_add=True,
    )

    def __str__(self):
        return f'Сообщение {self.pk} от {self.profile}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'