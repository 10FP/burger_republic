# Generated by Django 3.2.25 on 2024-09-24 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('burger_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('subscribed_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
