# Generated by Django 4.2.5 on 2023-12-10 06:34

from django.db import migrations, models
import main.misc


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_part_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='model',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='part',
            name='image',
            field=models.ImageField(default='images/default.png', upload_to=main.misc.get_upload_path),
        ),
    ]