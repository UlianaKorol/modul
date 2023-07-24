from django.db import models

class Advertisement(models.Model):
    # название товара
    # CharField - короткое текстовое поле
    # 'заголовок' - verbose_name - человекочитаемое название
    title = models.CharField('заголовок', max_length=128)

    # Описание товара
    # Длинное текстовое поле - TextField
    description = models.TextField('описание')

    # Цена
    # Числовое поле с фиксированной точкой 
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)

    # Уместен ли торг?
    # BooleanField - булевое поле (логическое) (окшн)
    auction = models.BooleanField('торг', help_text='Отметьте, если хотите торговаться')

    # дата публикации
    created_at = models.DateTimeField(auto_now_add=True)

    # Дата изменения/объявления + что изменилось
    updated_at = models.DateTimeField(auto_now=True)

    # Продавец (имя продавца, контакты для связи, отзывы)
    # Фото объявления
    # Рейтинг 
    # В продаже/не в продаже - актуальность
