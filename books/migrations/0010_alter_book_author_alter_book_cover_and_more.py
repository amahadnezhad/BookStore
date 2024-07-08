# Generated by Django 4.2.13 on 2024-07-08 11:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0009_alter_book_publisher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=200, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(blank=True, upload_to='covers/', verbose_name='Cover'),
        ),
        migrations.AlterField(
            model_name='book',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Datetime_Created'),
        ),
        migrations.AlterField(
            model_name='book',
            name='datetime_modified',
            field=models.DateTimeField(auto_now=True, verbose_name='Datetime_Modified'),
        ),
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is_Active'),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.PositiveIntegerField(verbose_name='Price'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=200, verbose_name='Publisher'),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='book',
            name='translator',
            field=models.CharField(blank=True, max_length=200, verbose_name='Translator'),
        ),
        migrations.AlterField(
            model_name='book',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Datetime_Created'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='Is-Active'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True, verbose_name='Recommend'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
    ]