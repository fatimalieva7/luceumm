
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

class BookCategory(models.Model):
    """Категории литературы (напр. Учебная, Художественная, Методическая)"""

    name = models.CharField(max_length=100, verbose_name="Название категории")

    class Meta:
        verbose_name = "Категория книг"
        verbose_name_plural = "Категории книг"

    def __str__(self):
        return self.name


class Book(models.Model):
    """Каталог книг и учебников"""

    title = models.CharField(max_length=255, verbose_name="Название книги")
    author = models.CharField(
        max_length=255, verbose_name="Автор", blank=True, null=True
    )
    category = models.ForeignKey(
        BookCategory,
        on_delete=models.CASCADE,
        verbose_name="Категория",
        related_name="books",
    )
    cover = models.ImageField(
        upload_to="library/covers/", verbose_name="Обложка", blank=True, null=True
    )
    description = models.TextField(verbose_name="Описание", blank=True)
    pdf_file = models.FileField(
        upload_to="library/pdfs/",
        verbose_name="Электронная версия (PDF)",
        blank=True,
        null=True,
    )
    is_available = models.BooleanField(
        default=True, verbose_name="Доступна в печатном виде"
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Каталог книг"

    def __str__(self):
        return self.title


class LibraryEvent(models.Model):
    """Мероприятия, лит. вечера, выставки"""

    title = models.CharField(
        max_length=255, verbose_name="Название мероприятия"
    )
    image = models.ImageField(
        upload_to="library/events/", verbose_name="Фото мероприятия"
    )
    description = models.TextField(verbose_name="Описание")
    event_date = models.DateTimeField(
        verbose_name="Дата и время проведения", blank=True, null=True
    )

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия и выставки"

    def __str__(self):
        return self.title


class DigitalResource(models.Model):
    """Полезные ссылки на внешние базы данных и электронные библиотеки"""

    title = models.CharField(
        max_length=255, verbose_name="Название ресурса/портала"
    )
    url = models.URLField(verbose_name="Ссылка на ресурс")
    description = models.CharField(
        max_length=300, verbose_name="Краткое описание"
    )
    icon_class = models.CharField(
        max_length=50,
        default="fa-globe",
        verbose_name="Иконка FontAwesome (напр. fa-book)",
    )

    class Meta:
        verbose_name = "Электронный ресурс"
        verbose_name_plural = "Электронные ресурсы"

    def __str__(self):
        return self.title





class DormitoryFeature(models.Model):
    """Удобства и преимущества общежития (Wi-Fi, Охрана, Кухня и т.д.)"""

    title = models.CharField(
        max_length=150, verbose_name="Название удобства"
    )
    description = models.CharField(
        max_length=255, verbose_name="Краткое описание"
    )
    icon_class = models.CharField(
        max_length=50,
        default="fa-wifi",
        verbose_name="Иконка FontAwesome (напр. fa-wifi, fa-shield-alt, fa-utensils)",
    )
    order = models.PositiveIntegerField(
        default=0, verbose_name="Порядок сортировки"
    )

    class Meta:
        verbose_name = "Удобство / Преимущество"
        verbose_name_plural = "Удобства общежития"
        ordering = ["order"]

    def __str__(self):
        return self.title


class DormitoryRoom(models.Model):
    """Типы комнат и зон (Комнаты проживания, Кухня, Зона отдыха и т.д.)"""

    title = models.CharField(
        max_length=150, verbose_name="Название зоны/комнаты"
    )
    capacity = models.CharField(
        max_length=100,
        verbose_name="Вместимость/Тип",
        blank=True,
        help_text="Например: '2-3 места', 'Общая зона', 'Для парней'",
    )
    image = models.ImageField(
        upload_to="dormitory/rooms/", verbose_name="Фотография"
    )
    description = models.TextField(verbose_name="Описание условий")
    is_active = models.BooleanField(default=True, verbose_name="Отображать")

    class Meta:
        verbose_name = "Комната / Помещение"
        verbose_name_plural = "Комнаты и помещения"

    def __str__(self):
        return self.title


class DormitoryRule(models.Model):
    """Правила и распорядок дня"""

    time_range = models.CharField(
        max_length=100,
        verbose_name="Время / Период",
        help_text="Например: '07:00 - 08:00' или 'После 22:00'",
    )
    title = models.CharField(max_length=200, verbose_name="Действие / Правило")
    description = models.TextField(
        verbose_name="Подробности", blank=True, null=True
    )

    class Meta:
        verbose_name = "Правило / Распорядок"
        verbose_name_plural = "Распорядок дня и правила"

    def __str__(self):
        return f"{self.time_range} — {self.title}"


class DormitoryFAQ(models.Model):
    """Часто задаваемые вопросы о проживании"""

    question = models.CharField(max_length=255, verbose_name="Вопрос")
    answer = models.TextField(verbose_name="Ответ")

    class Meta:
        verbose_name = "Вопрос-ответ (FAQ)"
        verbose_name_plural = "Вопросы и ответы (FAQ)"

    def __str__(self):
        return self.question

