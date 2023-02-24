from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


class TaskForm(forms.Form):
    title = forms.CharField(max_length=100, required=True, label='Заголовок')
    description = forms.CharField(max_length=3000, required=True, label='Описание', widget=widgets.Textarea)
    status = forms.CharField(max_length=50, required=True, label='Статус')
    ended_at = forms.DateTimeField(label='Дата выполнения', required=True)

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if len(title) < 2:
            raise ValidationError('Заголовок должен быть длинее 2-ух символов')
        return title
