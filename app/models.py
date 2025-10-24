from django.db import models

# Create your models here.
class Trainer (models.Model):
    ID = models.CharField(
        max_length=200,
    )

    profession = models.CharField(
        verbose_name ="Должность",
        max_length =200,
    )

    license = models.Charfield(
        verbose_name = "Лицензия",
        max_length =200,
    )

    XP = models.Charfield(
        verbose_name="Опыт работы",
        max_length=200,
    )

    class User(models.Model):
        ID = models.CharField(
            max_length=200,
        )

    name = models.CharField(
        verbose_name="ФИО",
        max_length=100,
    )

    number = models.IntegerField(
        verbose_name="Номер телефона",
        max_length=11,
    )

    name_kinder = models.CharField(
        verbose_name="ФИО ребенка"
        max_length=200
    )

    birthdate = models.DateField(
        verbose_name="Дата рождения",
        max_length=8,
    )

    class Children(models.Model):
        name = models.CharField(
            verbose_name="ФИО",
            max_length=200,
        )

        birthdate = models.DateField(
            verbose_name="Дата рождения",
            max_length=8
        )