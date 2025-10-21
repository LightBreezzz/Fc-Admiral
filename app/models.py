from django.db import models
from django.core.validators import RegexValidator


class Coach(models.Model):
    """Модель тренера"""
    full_name = models.CharField(max_length=200, verbose_name="ФИО")
    position = models.CharField(max_length=100, verbose_name="Должность")
    qualification = models.CharField(
        max_length=200, verbose_name="Квалификация"
    )
    work_experience = models.PositiveIntegerField(
        verbose_name="Опыт работы (лет)"
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

    class Meta:
        verbose_name = "Тренер"
        verbose_name_plural = "Тренеры"
        ordering = ['full_name']

    def __str__(self):
        return self.full_name


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


class Parent(models.Model):
    """Модель родителя/пользователя"""
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Номер телефона должен быть в формате: '+999999999'. "
                "До 15 цифр."
    )

    full_name = models.CharField(
        max_length=200, verbose_name="ФИО родителя"
    )
    phone = models.CharField(
        validators=[phone_regex], max_length=17, verbose_name="Телефон"
    )
    player = models.ForeignKey(
        Player, on_delete=models.CASCADE, verbose_name="Игрок",
        related_name='parents'
    )
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name="Дата создания"
    )
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления"
    )

    class Meta:
        verbose_name = "Родитель"
        verbose_name_plural = "Родители"
        ordering = ['full_name']

    def __str__(self):
        return f"{self.full_name} (родитель {self.player.full_name})"

    @property
    def player_full_name(self):
        """ФИО игрока"""
        return self.player.full_name

    @property
    def player_birth_date(self):
        """Дата рождения игрока"""
        return self.player.birth_date
