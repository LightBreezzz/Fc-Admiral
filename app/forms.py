# forms.py
from django import forms
from .models import JoinRequest


class JoinRequestForm(forms.ModelForm):
    """Форма заявки на пробную тренировку"""

    class Meta:
        model = JoinRequest
        fields = ['parent_full_name', 'parent_phone', 'child_full_name', 'child_birth_date', 'branch']
        widgets = {
            'parent_full_name': forms.TextInput(attrs={'placeholder': 'ФИО родителя*'}),
            'parent_phone': forms.TextInput(attrs={'placeholder': 'Контактный телефон*', 'type': 'tel'}),
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