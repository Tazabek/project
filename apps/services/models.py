from django.db import models
from django.shortcuts import reverse


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


class Service2(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    about = models.TextField(verbose_name='O категории')
    foto = models.ImageField(verbose_name='фото', upload_to='foto/', null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Service2 page'

class Service3(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название категории')
    about = models.TextField(verbose_name='O категории')
    foto = models.ImageField(verbose_name='фото', upload_to='foto/', null=True, blank=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'Service3 page'

class Plan(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название плана', null=True, blank=True)
    curs = models.CharField(verbose_name='Курс оплаты', max_length=10, null=True, blank=True)
    summ = models.DecimalField(verbose_name='Cymma oплаты ', decimal_places=2, max_digits=10)
    category = models.CharField(verbose_name='Категория', max_length=155, null=True, blank=True)
    color = models.CharField('цвет', max_length=15, blank=True, null=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'page Service3 План'

class Includes(models.Model):
    include = models.CharField(verbose_name='Что включает план', max_length=155, blank=True, null=True)
    plans = models.ForeignKey(Plan, on_delete=models.CASCADE, verbose_name='План')

    def __str__(self) -> str:
        return 'Что включает'

    class Meta:
        verbose_name_plural = 'Что включает'


class Service5(models.Model):
    name = models.CharField(verbose_name='Название услуги', max_length=155)
    desc = models.TextField(verbose_name='Описание услуги')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = 'page Service 5'


class IncludesServ(models.Model):
    include = models.CharField(verbose_name='Что включает план', max_length=155, blank=True, null=True)
    servs = models.ForeignKey(Service5, on_delete=models.CASCADE, verbose_name='План')

    def __str__(self) -> str:
        return 'Что включает'

    class Meta:
        verbose_name_plural = 'Что включает услуга'



