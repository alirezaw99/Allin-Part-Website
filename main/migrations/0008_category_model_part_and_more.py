# Generated by Django 4.2.5 on 2023-12-03 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_auto_washing_machine_part_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('model_brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('part_number', models.CharField(max_length=15)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField(null=True)),
                ('in_stock', models.BooleanField(default=False)),
                ('is_onsale', models.BooleanField(default=False)),
                ('discounted_price', models.PositiveIntegerField(default=0)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(to='main.category')),
                ('tags', models.ManyToManyField(to='main.tag')),
                ('used_models', models.ManyToManyField(to='main.model')),
            ],
        ),
        migrations.RemoveField(
            model_name='auto_washing_machine_part',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='auto_washing_machine_part',
            name='used_models',
        ),
        migrations.DeleteModel(
            name='Auto_Washing_Machine_Model',
        ),
        migrations.DeleteModel(
            name='Auto_Washing_Machine_Part',
        ),
    ]
