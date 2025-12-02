from django.db import models
from django.core.validators import (
    RegexValidator, MinValueValidator, MaxValueValidator
)
from datetime import datetime


class Coach(models.Model):
    """Модель тренера"""
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    qualification = models.CharField(
        max_length=200, verbose_name="Лицензия"
    )
    education = models.CharField(
        max_length=200, verbose_name="Образование", blank=True, null=True
    )
    work_start_year = models.IntegerField(
        verbose_name="Опыт работы (с года)",
        help_text="Год начала работы тренером",
        validators=[
            MinValueValidator(
                1950, message="Год не может быть раньше 1950"
            ),
            MaxValueValidator(
                datetime.now().year,
                message="Год не может быть больше текущего"
            )
        ],
        blank=True, null=True
    )
    photo = models.ImageField(
        upload_to='coaches/', blank=True, null=True, verbose_name="Фото"
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    order = models.PositiveIntegerField("Порядок", default=0, blank=True)

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"
        ordering = ['order', 'full_name']

    def __str__(self):
        return self.full_name

    def get_name_parts(self):
        """Разделяет ФИО на фамилию и имя+отчество"""
        parts = self.full_name.split()
        if len(parts) >= 2:
            return {
                'surname': parts[0],
                'name': ' '.join(parts[1:])
            }
        return {
            'surname': self.full_name,
            'name': ''
        }


class Player(models.Model):
    """Модель игрока"""
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    birth_date = models.DateField(verbose_name="Дата рождения")
    photo = models.ImageField(
        upload_to='players/', blank=True, null=True, verbose_name="Фото"
    )
    coach = models.ForeignKey(
        Coach, on_delete=models.SET_NULL, null=True, blank=True,
        verbose_name="Тренер", related_name='players'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Игрок"
        verbose_name_plural = "Игроки"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name

    @property
    def age(self):
        """Возраст игрока"""
        from datetime import date
        today = date.today()
        return (today.year - self.birth_date.year -
                ((today.month, today.day) <
                 (self.birth_date.month, self.birth_date.day)))

    def get_name_parts(self):
        """Разделяет ФИО на фамилию и имя+отчество"""
        parts = self.full_name.split()
        if len(parts) >= 2:
            return {
                'surname': parts[0],
                'name': ' '.join(parts[1:])
            }
        return {
            'surname': self.full_name,
            'name': ''
        }


class JoinRequest(models.Model):
    """Заявка на пробную тренировку"""

    # Валидатор для телефона
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+999999999'. До 15 цифр."
    )

    # Поля из анкеты
    parent_full_name = models.CharField(
        max_length=200,
        verbose_name="ФИО родителя"
    )
    parent_phone = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name="Контактный телефон"
    )
    child_full_name = models.CharField(
        max_length=200,
        verbose_name="ФИО ребёнка"
    )
    child_birth_date = models.DateField(
        verbose_name="Дата рождения ребёнка"
    )
    branch = models.CharField(
        max_length=100,
        choices=[
            ('', 'Выбрать отделение'),
            ('centr', 'Царицыно'),
            ('sever', 'Коломенская'),
        ],
        verbose_name="Отделение"
    )

    # Дополнительные поля (не обязательные, но полезные)
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Заявка на тренировку"
        verbose_name_plural = "Заявки на тренировку"
        ordering = ['-created_at']  # новые заявки сверху

    def __str__(self):
        return f"{self.parent_full_name} → {self.child_full_name} ({self.branch})"

    @property
    def player_full_name(self):
        """ФИО игрока"""
        return self.player.full_name

    @property
    def player_birth_date(self):
        """Дата рождения игрока"""
        return self.player.birth_date
