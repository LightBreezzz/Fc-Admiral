# forms.py
from django import forms
from django.core.exceptions import ValidationError
from .models import JoinRequest
import re


def validate_name(value: str) -> None:
    """Разрешаем только русские буквы и пробелы."""
    if not re.match(r'^[А-Яа-яЁё\s]+$', value):
        raise ValidationError(
            'Имя должно содержать только русские буквы и пробелы'
        )


class JoinRequestForm(forms.ModelForm):
    """Форма заявки на пробную тренировку."""

    parent_full_name = forms.CharField(
        validators=[validate_name],
        widget=forms.TextInput(
            attrs={
                'class': 'anceta__input',
                'placeholder': 'ФИО родителя*',
            }
        ),
        label='',
    )

    parent_phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'anceta__input',
                'type': 'tel',
                'placeholder': '+7 (999) 999-99-99',
                'inputmode': 'tel',
            }
        ),
        label='',
    )

    child_birth_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',  # нативный календарь
                'class': 'anceta__input',
                'placeholder': 'ДД.ММ.ГГГГ',
            }
        ),
        label='',
        input_formats=['%Y-%m-%d'],
    )

    class Meta:
        model = JoinRequest
        fields = [
            'parent_full_name',
            'parent_phone',
            'child_full_name',
            'child_birth_date',
            'branch',
        ]
        widgets = {
            'child_full_name': forms.TextInput(
                attrs={
                    'class': 'anceta__input',
                    'placeholder': 'ФИО ребёнка*',
                }
            ),
            # branch рендерится через кастомный select в шаблоне,
            # поэтому отдельный widget не задаём.
        }
        labels = {
            'child_full_name': '',
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

    def clean_parent_phone(self):
        value = self.cleaned_data.get('parent_phone', '')
        if not value:
            raise forms.ValidationError("Пожалуйста, укажите телефон.")
        digits = re.sub(r'\D', '', value)
        if digits.startswith('8') and len(digits) == 11:
            digits = '7' + digits[1:]
        if len(digits) != 11 or not digits.startswith('7'):
            raise forms.ValidationError(
                'Номер должен быть в формате: +7 (999) 999-99-99'
            )
        return f"+{digits}"
