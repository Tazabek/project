from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField

#block0
class Slides(models.Model):
    s1word1 = models.CharField(max_length=30, verbose_name='первое слово слайда 1')
    s1word2 = models.CharField(max_length=30, verbose_name='второе слово слайда 1')
    s1word3 = models.CharField(max_length=30, verbose_name='третье слово слайда 1')
    s1word4 = models.CharField(max_length=30, verbose_name='четвертое слово слайда 1')
    s1word5 = models.CharField(max_length=30, verbose_name='пятое слово слайда 1')
    s2word1 = models.CharField(max_length=30, verbose_name='первое слово слайда 2')
    s2word2 = models.CharField(max_length=30, verbose_name='второе слово слайда 2')
    s2word3 = models.CharField(max_length=30, verbose_name='третье слово слайда 2')
    s3word1 = models.CharField(max_length=30, verbose_name='первое слово слайда 3')
    s3word2 = models.CharField(max_length=30, verbose_name='второе слово слайда 3')
    s3word3 = models.CharField(max_length=30, verbose_name='третье слово слайда 3')

    def __str__(self) -> str:
        return 'Cлова слайдов'

    class Meta:
        verbose_name_plural = 'block0 Слайды'


#block1
class Block1(models.Model):
    about = models.TextField(verbose_name='о нас', help_text='например: наша компания одна из лучших')
    sentences1 = models.TextField(verbose_name='Предложения')
    feachered = models.TextField(verbose_name='Подчеркнутое предложение')
    sentences2 = models.TextField(verbose_name='Предложения')

    def __str__(self) -> str:
        return 'О нас'

    class Meta:
        verbose_name_plural = 'block1 О нас'


#block2
class CategoryPortfolio(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    about = models.TextField(verbose_name='O категории')
    foto = models.ImageField(verbose_name='фото', upload_to='foto/', null=True)
    slug = models.SlugField(verbose_name='Ссылка', max_length=30)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("category", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name_plural = 'block2 Категории'


#block3
class Services(models.Model):
    name = models.CharField(verbose_name='название услуги', max_length=50)
    about = models.TextField(verbose_name='Описание')
    slug = models.SlugField(verbose_name='Ссылка', max_length=30)
    foto = models.ImageField(verbose_name='фото', upload_to='service/', null=True, blank=True)
    number = models.IntegerField(verbose_name='номер', unique=True)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("service", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name_plural = 'block3 Услуги'


#Block4
class Portfolio(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название портфолио')
    foto = models.ImageField(verbose_name='фото', upload_to='fotos/', null=True, blank=True)
    about = models.TextField(verbose_name='Описание', null=True, blank=True)
    slug = models.SlugField(verbose_name='Ссылка', max_length=30)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("portfolio", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name_plural = 'block4 Портфолио'



class Advertisement(models.Model):
    name = models.CharField(verbose_name='Название рекламы', max_length=255)
    desc = models.TextField(verbose_name='Описание рекламы')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'block6 Реклама'

class Images(models.Model):
    name_on_image = models.CharField(max_length=155, verbose_name='Название на фото')
    text_on_image = models.TextField(verbose_name='Текст на фото')
    image = models.ImageField(verbose_name='фото', upload_to='advertisement', null=True, blank=True)
    slug = models.SlugField(verbose_name='Ссылка')
    advert = models.ForeignKey(Advertisement, on_delete=models.CASCADE, verbose_name='реклаma')

    def get_absolute_url(self):
        return reverse("advertisements", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.advert.name

    class Meta:
        verbose_name_plural = 'Фото рекламы'


class Reviews(models.Model):
    name = models.CharField(max_length=155, verbose_name='Имя автора')
    job = models.CharField(max_length=155, verbose_name='Должность автора')
    image = models.ImageField(verbose_name='Фотот автора', upload_to='reviews/', null=True, blank=True)
    text = models.TextField(verbose_name='Tekct')
    slug = models.SlugField(verbose_name='Ссылка')

    def get_absolute_url(self):
        return reverse("reviews", kwargs={"slug": self.slug})

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Block8 Отзывы'


class Contacts(models.Model):
    head_phone = models.CharField('Первый номер', max_length=20)
    tel_nums_newacc = models.CharField('Номер телефона для новых аккаунтов', max_length=15)
    tel_nums_support = models.CharField('Служба поддержки', max_length=15)
    first_email = models.EmailField(verbose_name='почта')
    second_email = models.EmailField(verbose_name='почта2')
    adress = models.CharField(max_length=255, verbose_name='Адресс')
    youtube = models.CharField(verbose_name='Ссылка на youtube', max_length=155)
    twitter = models.CharField(verbose_name='Ссылка на twitter', max_length=155)
    facebook = models.CharField(verbose_name='Ссылка на facebook', max_length=155)
    linkedin = models.CharField(verbose_name='Ссылка на linkedin', max_length=155)
    google = models.CharField(verbose_name='Ссылка на google', max_length=155)

    def __str__(self) -> str:
        return 'Контакты'

    class Meta:
        verbose_name_plural = 'Block10 Контакты'


class About(models.Model):
    quote = models.TextField(verbose_name='Цитата')
    theme1 = models.CharField(verbose_name='Тема текста 1', max_length=255)
    text1 = models.TextField(verbose_name='Текст 1')
    theme2 = models.CharField(verbose_name='Тема текста 2', max_length=255)
    text2 = models.TextField(verbose_name='Текст 2')
    theme3 = models.CharField(verbose_name='Тема текста 3', max_length=255)
    text3 = models.TextField(verbose_name='Текст 3')

    def __str__(self) -> str:
        return 'О нас'

    class Meta:
        verbose_name_plural = 'О нас страница'



TAG_NEWS_CHOICES = [
    ('recent', 'recent'),
    ('others', 'others')
]

class Posts(models.Model):
    tag = models.CharField('Тег', choices=TAG_NEWS_CHOICES, max_length=30)
    date = models.DateField('Дата', auto_now=False, auto_now_add=False)
    img = models.ImageField('Фото', upload_to='images/')
    name = models.CharField(max_length=255, verbose_name='Название')
    desc = RichTextField('Описание')

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ['-id',]
        verbose_name_plural = 'Публикации'