# Generated by Django 3.2.12 on 2022-05-17 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employers',
            name='description',
            field=models.TextField(blank=True, help_text='О сотруднике', null=True, verbose_name='О сотруднике'),
        ),
        migrations.AlterField(
            model_name='employers',
            name='image',
            field=models.ImageField(blank=True, help_text='Фото сотрудника', null=True, upload_to='images/employers', verbose_name='Фото сотрудника'),
        ),
        migrations.AlterField(
            model_name='employers',
            name='name',
            field=models.CharField(help_text='Имя и Фамилия', max_length=50, verbose_name='Имя и Фамилия'),
        ),
        migrations.AlterField(
            model_name='employers',
            name='position',
            field=models.CharField(help_text='Должность', max_length=50, verbose_name='Должность'),
        ),
        migrations.AlterField(
            model_name='employers',
            name='work_since',
            field=models.DateTimeField(blank=True, help_text='Дата устройства в компани.', null=True, verbose_name='Устроился  в компанию'),
        ),
    ]
