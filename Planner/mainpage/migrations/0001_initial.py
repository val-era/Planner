# Generated by Django 4.1.4 on 2022-12-23 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название задачи')),
                ('task', models.CharField(max_length=300, verbose_name='Задача')),
                ('teg', models.CharField(choices=[('Работа', '💻 Работа'), ('Спорт', '🏆 Спорт'), ('Семья', '👫 Семья'), ('Личная', '🎧 Личная'), ('Обучение', '🎓 Обучение'), ('Дом', '🏰 Дом'), ('Здоровье', '🧬 Здоровье'), ('Путешествия', '🌋 Путешествия'), ('Отдых', '🎮 Отдых'), ('Покупки', '🍕 Покупки'), ('Мероприятия', '🎪 Мероприятия'), ('Другое', '🚇 Другое'), ('', '')], default='', max_length=11, verbose_name='Тег')),
                ('date', models.DateField(verbose_name='Дата Задачи')),
                ('is_global', models.BooleanField(verbose_name='Отнести к задаче')),
                ('global_task', models.CharField(blank=True, max_length=100, verbose_name='Глобальная задача')),
            ],
            options={
                'verbose_name': 'Задача',
                'verbose_name_plural': 'Задачи',
            },
        ),
    ]
