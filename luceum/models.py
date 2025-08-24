from django.db import models


class HeroSection(models.Model):
    image = models.ImageField(upload_to='hero/', blank=True, null=True, verbose_name='Изображение')
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    button_primary_text = models.CharField(max_length=50, verbose_name="Переход о нас")
    button_primary_url = models.CharField(max_length=200, verbose_name="Ссылка на регистрацию")

    def __str__(self):
        return self.title


class Cotegory(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Название категории')
    description = models.TextField(blank=True, null=True, verbose_name='Описание категории')
    image = models.ImageField(upload_to='categories/', blank=True, null=True, verbose_name='Изображение категории')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг категории')

    def __str__(self):
        return self.name

class Profesion(models.Model):
    name = models.CharField(max_length=100, unique=20,verbose_name='Название профессии')
    description = models.TextField(blank=True, null=True, verbose_name='Описание профессии')
    image = models.ImageField(upload_to='professions/', blank=True, null=True,verbose_name='Изображение профессии')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг профессии')


    def __str__(self):
        return self.name

class Pedagog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя педагога')
    image = models.ImageField(upload_to='pedagogs/', blank=True, null=True, verbose_name='Изображение педагога')
    discription = models.TextField(blank=True, null=True, verbose_name='Описание педагога')
    

    def __str__(self):
        return self.name


class Bestpedagog(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя лучшего педагога')
    image = models.ImageField(upload_to='bestpedagogs/', blank=True, null=True, verbose_name='Изображение лучшего педагога')
    description = models.TextField(blank=True, null=True, verbose_name='Описание лучшего педагога')

    def __str__(self):
        return self.name

class Curss(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название курса')
    duration = models.CharField(max_length=100, verbose_name='Длительность курса',blank=True,null=True)
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
