from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва категорії")
    description = models.TextField(blank=True, null=True, verbose_name="Опис категорії")

    def __str__(self):
        return self.name

class Task(models.Model):
    STATUS_CHOICES = [
        ('new', 'Нове'),
        ('in_progress', 'В роботі'),
        ('completed', 'Завершено'),
    ]

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    description = models.TextField(verbose_name="Опис")
    deadline = models.DateTimeField(verbose_name="Дедлайн")
    priority = models.IntegerField(verbose_name="Пріоритет")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return self.title
