import datetime

from .models import Tasks
from django.forms import ModelForm, TextInput, DateInput, DateField, Form, CharField


class TaskForm(ModelForm):
    class Meta:
        model = Tasks
        fields = ['title', 'task', 'teg', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Заголовок задачи',
            }),
            "task": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Задача',
            }),
            "date": DateInput(attrs={
                'type': 'date',
                'value': datetime.date.today(),
                'min': "2022-01-01",
                'max': "2030-12-31",
            })
        }


class DateForm(Form):
    date = DateField(label='Выберите дату для переноса',
        input_formats=['%d/%m/%Y %H:%M'],
        widget=DateInput(attrs={
            'type': 'date',
                'min': "2022-01-01",
                'max': "2030-12-31",

        })
    )
    id = CharField( widget=TextInput(attrs={
        "type": "text",

    }))

class GlobalForm(Form):
    global_add = CharField(label="Добавить Глобальную задачу", required=False,
    widget = TextInput(attrs={
        'type': 'text',
        'placeholder': 'Добавить в новый проект',
    })
    )

    idtask = CharField(widget=TextInput(attrs={
                        'type': 'text',
    })
    )

    sel = CharField(widget=TextInput(attrs={
                               'type': 'text',
    })
    )


class TagsForm(ModelForm):
    date = DateField(label='Выберите дату, при необходимости', required=False,
                     input_formats=['%d/%m/%Y %H:%M'],
                     widget=DateInput(attrs={
                         'type': 'date',
                         'min': "2022-01-01",
                         'max': "2030-12-31",

                     })
                     )
    class Meta:
        model = Tasks
        fields = ['teg']

