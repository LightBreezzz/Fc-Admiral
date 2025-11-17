from django import forms

from .models import JoinRequest


class JoinRequestForm(forms.ModelForm):
    """Форма заявки на пробную тренировку"""

    child_birth_date = forms.DateField(
        input_formats=['%d.%m.%Y', '%Y-%m-%d'],
        widget=forms.TextInput(
            attrs={
                'type': 'text',
                'class': 'anceta__input',
                'placeholder': 'дд.мм.гггг*',
                'required': 'required',
            }
        ),
        label="Дата рождения ребенка"
    )
    
    branch = forms.ChoiceField(
        choices=[('', 'Выбрать отделение*')] + list(JoinRequest.BRANCH_CHOICES),
        required=True,
        widget=forms.Select(
            attrs={
                'class': 'anceta__input anceta__select',
                'required': 'required',
            }
        ),
        label="Отделение"
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
            'parent_full_name': forms.TextInput(
                attrs={
                    'placeholder': 'ФИО родителя*',
                    'class': 'anceta__input',
                    'required': 'required',
                }
            ),
            'parent_phone': forms.TextInput(
                attrs={
                    'placeholder': 'Контактный телефон*',
                    'class': 'anceta__input',
                    'type': 'tel',
                    'required': 'required',
                }
            ),
            'child_full_name': forms.TextInput(
                attrs={
                    'placeholder': 'ФИО ребенка*',
                    'class': 'anceta__input',
                    'required': 'required',
                }
            ),
        }
        labels = {
            'parent_full_name': '',
            'parent_phone': '',
            'child_full_name': '',
            'child_birth_date': '',
            'branch': '',
        }

    def clean_branch(self):
        value = self.cleaned_data.get('branch')
        if not value:
            raise forms.ValidationError("Пожалуйста, выберите отделение.")
        return value

