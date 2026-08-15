from django.db import models



class Hero(models.Model):
   
    
    image = models.ImageField("Фотография", upload_to="hero_images/")
    created_at = models.DateTimeField("Дата публикации", auto_now_add=True)

    class Meta:
        verbose_name = "Слайд на главной"
        verbose_name_plural = "Слайды на главной"
        ordering = ['-created_at'] # Свежие новости будут первыми

    def __str__(self):
        return self.title

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


class Professi(models.Model):
    name = models.CharField(max_length=100, unique=20, verbose_name='Название профессии')
    description = models.TextField(blank=True, null=True, verbose_name='Описание профессии')
    image = models.ImageField(upload_to='professions/', blank=True, null=True, verbose_name='Изображение профессии')
    slug = models.SlugField(max_length=100, unique=True, verbose_name='Слаг профессии')




