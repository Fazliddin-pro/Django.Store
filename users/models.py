from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField

class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, null=True, verbose_name='Аватар')  # Загружаем изображение
    country = CountryField(blank_label='Выберите страну', null=True, blank=True, verbose_name='Страна')  # Страна с кодом
    address = models.TextField(blank=True, null=True, verbose_name='Адрес')  # Адрес пользователя
    phone_number = PhoneNumberField(
        null=True, 
        blank=True, 
        unique=True, 
        help_text='Введите номер телефона в международном формате, включая код страны',
        verbose_name='Номер'
    )  # Телефон с валидацией

    class Meta:
        db_table = 'user'
        verbose_name = 'Позлователя'
        verbose_name_plural = 'Позлователи'

    def __str__(self):
        return self.username
