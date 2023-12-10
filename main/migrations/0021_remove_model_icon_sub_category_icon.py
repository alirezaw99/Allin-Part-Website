# Generated by Django 4.2.5 on 2023-12-10 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_model_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='model',
            name='icon',
        ),
        migrations.AddField(
            model_name='sub_category',
            name='icon',
            field=models.ImageField(default='images/default.png', upload_to='category_icons'),
        ),
    ]
