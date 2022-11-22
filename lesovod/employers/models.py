from django.db import models


class Employers(models.Model):
    position = models.CharField(
        help_text='Должность',
        verbose_name='Должность',
        max_length=50,
    )
    name = models.CharField(
        help_text='Имя и Фамилия',
        verbose_name='Имя и Фамилия',
        max_length=50,
    )
    work_since = models.DateTimeField(
        help_text='Дата устройства в компани.',
        verbose_name='Устроился  в компанию',
        auto_now_add=False,
        null=True,
        blank=True
    )
    description = models.TextField(
        help_text='О сотруднике',
        verbose_name='О сотруднике',
        null=True,
        blank=True,
    )
    image = models.ImageField(
        help_text='Фото сотрудника',
        verbose_name='Фото сотрудника',
        upload_to='images/employers',
        null=True,
        blank=True,

    )

    def __str__(self) -> str:
        return str(self.description)
