# Generated by Django 3.2.25 on 2024-09-27 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_app', '0005_alter_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuDrink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu_drinks/')),
            ],
        ),
        migrations.CreateModel(
            name='MenuFries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='menu_fries/')),
            ],
        ),
    ]
