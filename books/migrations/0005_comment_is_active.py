# Generated by Django 4.2.13 on 2024-06-27 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_comment_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
