from django.db import models
from django.shortcuts import reverse
from ckeditor.fields import RichTextField

class SingleService1(models.Model):
    image = models.ImageField('Фото', upload_to='image/')
    text_theme = models.CharField('тема текста', max_length=155, blank=True, null=True)
    text = RichTextField()

    def __str__(self) -> str:
        return 'Singe_service 1'

    class Meta:
        verbose_name_plural = 'Single_service 1'

class OtherServs(models.Model):
    name = models.CharField('Название услуги', max_length=155, blank=True, null=True)
    experience = models.CharField('Название сферы', max_length=155, blank=True, null=True)
    advantages = models.CharField('Приимущества', max_length=155, blank=True, null=True)
    percent = models.CharField('Проценты', max_length=5, blank=True, null=True)
    slug = models.SlugField('Ссылка', max_length=30)
    service = models.ForeignKey(SingleService1, on_delete=models.CASCADE, verbose_name='page')


    def __str__(self) -> str:
        return 'График'

    def get_absolute_url(self):
        return reverse("other_servs", kwargs={"slug": self.slug})
    
    class Meta:
        verbose_name_plural = 'График в тексте'

class Comments(models.Model):
    name = models.CharField('имя', max_length=155)
    proffession = models.CharField('должность', max_length=155)
    text = models.TextField('текст')
    service = models.ForeignKey(SingleService1, on_delete=models.CASCADE)
    image = models.ImageField('Фото', upload_to='comments/', blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Комменты'


class SingleService2(models.Model):
    image = models.ImageField('Фото', upload_to='image/')
    text = RichTextField('Текст')

    def __str__(self) -> str:
        return 'Singe_service 2'

    class Meta:
        verbose_name_plural = 'Single_service 2'


class Plan(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название плана', null=True, blank=True)
    curs = models.CharField(verbose_name='Курс оплаты', max_length=10, null=True, blank=True)
    summ = models.DecimalField(verbose_name='Cymma oплаты ', decimal_places=2, max_digits=10)
    category = models.CharField(verbose_name='Категория', max_length=155, null=True, blank=True)
    color = models.CharField('цвет', max_length=15, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Single_Service2 План'

class Includes(models.Model):
    include = models.CharField(verbose_name='Что включает план', max_length=155, blank=True, null=True)
    plans = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name='План')

    def __str__(self) -> str:
        return 'Что включает'

    class Meta:
        verbose_name_plural = 'Что включает'

class Contacts(models.Model):
    youtube = models.CharField(verbose_name='Ссылка на youtube', max_length=155)
    twitter = models.CharField(verbose_name='Ссылка на twitter', max_length=155)
    facebook = models.CharField(verbose_name='Ссылка на facebook', max_length=155)
    linkedin = models.CharField(verbose_name='Ссылка на linkedin', max_length=155)
    google = models.CharField(verbose_name='Ссылка на google', max_length=155)
    service = models.ForeignKey(SingleService2, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return 'Контакты'

    class Meta:
        verbose_name_plural = 'Single_service2 Контакты'