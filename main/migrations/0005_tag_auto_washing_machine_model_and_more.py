# Generated by Django 4.2.5 on 2023-12-02 11:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_rename_brands_brand'),
    ]

    operations = [
        migrations.CreateModel(
            name='tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Auto_Washing_Machine_Model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=255)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('model_brand', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.brand')),
            ],
        ),
        migrations.CreateModel(
            name='Auot_Washing_Machine_Part',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('part_number', models.CharField(max_length=15)),
                ('price', models.PositiveIntegerField()),
                ('description', models.TextField()),
                ('in_stock', models.BooleanField(default=False)),
                ('is_onsale', models.BooleanField(default=False)),
                ('discounted_price', models.PositiveIntegerField(null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('edited_date', models.DateTimeField(auto_now=True)),
                ('tags', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.tag')),
                ('used_models', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.auto_washing_machine_model')),
            ],
        ),
    ]
