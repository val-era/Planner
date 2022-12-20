from django.db import models

class Tasks(models.Model):
    user_name = models.TextField("Имя")
    title = models.TextField("Название задачи")
    task = models.TextField("Задача")
    teg = models.TextField("Тэг")
    date = models.DateField('Дата Задачи')
    is_global = models.BooleanField('is_global_task')
    global_task = models.TextField("Глобальная задача")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

