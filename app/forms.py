# forms.py
from django import forms
from .models import JoinRequest
import re
from django.core.exceptions import ValidationError


def validate_phone(value):
    if not re.match(r'^\+7\s?\(\d{3}\)\s?\d{3}-\d{2}-\d{2}$', value):
        raise ValidationError('Номер должен быть в формате: +7 (999) 999-99-99')


# В классе формы:
parent_phone = forms.CharField(
    validators=[validate_phone],
    widget=forms.TextInput(attrs={
        'class': 'anceta__input',
        'placeholder': '+7 (999) 999-99-99',
        'inputmode': 'tel'  # ← это даёт цифровую клавиатуру на мобилках
    })
)


def validate_name(value):
    if not re.match(r'^[а-яА-ЯёЁ\s]+$', value):
        raise ValidationError('Имя должно содержать только русские буквы и пробелы')


# В форме:
parent_full_name = forms.CharField(
    validators=[validate_name],
    widget=forms.TextInput(attrs={'class': 'anceta__input', 'placeholder': 'ФИО родителя'})
)


class JoinRequestForm(forms.ModelForm):
    """Форма заявки на пробную тренировку"""
    child_birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',  # ← браузер покажет нативный календарь
                'class': 'anceta__input',
                'placeholder': 'ДД.ММ.ГГГГ'
            }
        ),
        label='Дата рождения ребёнка',
        input_formats=['%Y-%m-%d']  # формат, который отправляется
    )

    class Meta:
        model = JoinRequest
        fields = ['parent_full_name', 'parent_phone', 'child_full_name', 'child_birth_date', 'branch']
        widgets = {
            'parent_full_name': forms.TextInput(attrs={'placeholder': 'ФИО родителя*'}),
            'parent_phone': forms.TextInput(attrs={'type': 'tel', 'class': 'anceta__input', 'placeholder': 'Контактный телефон*'}),
            'child_full_name': forms.TextInput(attrs={'placeholder': 'ФИО ребенка*'}),
            'child_birth_date': forms.TextInput(attrs={'placeholder': 'дд.мм.гггг*'}),
            'branch': forms.Select(attrs={'placeholder': 'anceta_input anceta_select'}),
        }
        labels = {
            'parent_full_name': '',
            'parent_phone': '',
            'child_full_name': '',
            'child_birth_date': '',
            'branch': '',
        }

    def clean_child_birth_date(self):
        value = self.cleaned_data.get('child_birth_date')
        if not value:
            raise forms.ValidationError("Пожалуйста, укажите дату рождения.")
        return value

    def clean_branch(self):
        value = self.cleaned_data.get('branch')
        if not value:
            raise forms.ValidationError("Пожалуйста, выберите отделение.")
        return value