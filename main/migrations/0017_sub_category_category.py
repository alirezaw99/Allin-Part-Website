# Generated by Django 4.2.5 on 2023-12-06 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_alter_category_options_alter_sub_category_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='sub_category',
            name='category',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='main.category'),
            preserve_default=False,
        ),
    ]