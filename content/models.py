
from django.db import models


class InstitutionHistory(models.Model):
    """Модель для истории учреждения"""
    title = models.CharField(max_length=200, verbose_name="Заголовок истории")
    description = models.TextField(verbose_name="Описание истории", max_length=2000)


    class Meta:
        verbose_name = "История учреждения"
        verbose_name_plural = "История учреждения"
    def __str__(self):
        return f" {self.title}"

class Achievement(models.Model):
    """Модель для достижений лицея"""
    description = models.TextField(verbose_name="Описание достижения")

    class Meta:
        verbose_name_plural = "Достижения"

    def __str__(self):
        return self.title


class Profession(models.Model):
    name = models.CharField(max_length=100, unique=20, verbose_name='Название профессии')
    description = models.TextField(blank=True, null=True, verbose_name='Описание профессии')
    image = models.ImageField(upload_to='professions/', blank=True, null=True, verbose_name='Изображение профессии')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг профессии')

    def __str__(self):
        return self.name


class Pedagog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя педагога')
    image = models.ImageField(upload_to='pedagogs/', blank=True, null=True, verbose_name='Изображение педагога')
    discription = models.TextField(blank=True, null=True, verbose_name='Описание педагога')

    def __str__(self):
        return self.name

class Courses(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    duration = models.CharField(max_length=100, verbose_name='Длительность курса', blank=True, null=True)
    image = models.ImageField(upload_to='courses/', blank=True, null=True, verbose_name='Изображение курса')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена курса')

    def __str__(self):
        return self.name


class About(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название учреждения')
    description = models.TextField(verbose_name='Текст о лицее')
    title = models.CharField(max_length=100, verbose_name='Тема маркера')
    title2 = models.CharField(max_length=100, verbose_name='Подзаголовки')

    def __str__(self):
        return self.name

