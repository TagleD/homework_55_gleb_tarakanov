# Generated by Django 4.1.6 on 2023-02-15 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Заголовок')),
                ('description', models.TextField(max_length=3000, verbose_name='Описание')),
                ('status', models.CharField(default='new', max_length=50, verbose_name='Автор')),
                ('ended_at', models.DateTimeField(verbose_name='Срок выполнения')),
            ],
        ),
    ]