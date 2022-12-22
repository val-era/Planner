from django.db import models

class Tasks(models.Model):
    tag_choices = (("Работа", " Работа"), ("Спорт", "Спорт"),
                   ("Семья", "Семья"), ("Личная", "Личная"),
                   ("Обучение", "Обучение"), ("Дом", "Дом"),
                   ("Здоровье", "Здоровье"), ("Путешествия", "Путешествия"),
                   ("Отдых", "Отдых"), ("Покупки", "Покупки"),
                   ("Мероприятия", "Мероприятия"), ("Другое", "Другое"), ("", ""))

    title = models.CharField("Название задачи", max_length=100)
    task = models.CharField("Задача", max_length=300)
    teg = models.CharField("Тег", max_length=11, choices=tag_choices, default="")
    date = models.DateField('Дата Задачи')
    is_global = models.BooleanField('Отнести к задаче')
    global_task = models.CharField("Глобальная задача", null=True, max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

