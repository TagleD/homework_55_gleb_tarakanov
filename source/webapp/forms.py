from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets

from webapp.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'description', 'status', 'ended_at')
        labels = {
            'title': 'Заголовок задачи',
            'description': 'Описание задачи',
            'status': 'Статус',
            'ended_at': 'Срок выполнения'
        }
        help_texts = {
            "ended_at":  "Введите дату в формате YYYY-MM-DD!"
        }

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2-ух символов')
        return title

