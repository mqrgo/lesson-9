from django.db import models
from django.contrib.auth.models import User
from slugify import slugify
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=30,
        verbose_name='Категория',
        unique=True,
    )
    slug = models.SlugField(unique=True, editable=False, null=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("news:index_with_category", args=[self.slug])

    def save(self, *ar, **kw):
        self.slug = slugify(self.name)
        super().save(*ar, **kw)


# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок',
    )
    cover = models.ImageField(
        upload_to='news_covers/%Y/%m/%d',
        null=True,
        blank=True,
    )
    body = models.TextField(
        verbose_name='Текст новости'
    )
    created = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True,
    )
    author = models.ForeignKey(
        User,
        related_name='author',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Автор',
    )
    slug = models.SlugField(
        verbose_name='Слаг',
        unique_for_date='created',
        editable=False,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        verbose_name='Категория',
    )

    class Meta:
        ordering = ['-created']
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.title

    def save(self, *ar, **kw):
        self.slug = slugify(self.title)
        super().save(*ar, **kw)

    def get_absolute_url(self):
        url = reverse('news:detail', args=[
            self.created.year,
            self.created.month,
            self.created.day,
            self.slug,
        ])
        print(url)
        return url
