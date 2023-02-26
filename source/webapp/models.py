from django.db import models
from django.db.models import TextChoices


# Create your models here.

class StatusChoice(TextChoices):
    NEW = 'New', 'Новая'
    IN_PROGRESS = 'In Progress', 'В процессе'
    ENDED = 'Ended', 'Выполнена'

class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False, verbose_name="Заголовок")
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=20, verbose_name="Статус", choices=StatusChoice.choices, default=StatusChoice.NEW)
    ended_at = models.DateTimeField(verbose_name="Срок выполнения")

    def __str__(self):
        return f'{self.title} - {self.description}'