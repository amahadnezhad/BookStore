# Generated by Django 4.2.13 on 2024-06-27 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_comment_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='recommend',
            field=models.BooleanField(default=True),
        ),
    ]