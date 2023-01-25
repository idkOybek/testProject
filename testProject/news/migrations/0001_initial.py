# Generated by Django 5.0.dev20230124092027 on 2023-01-24 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='news',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('contentText', models.TextField(blank=True)),
                ('author', models.CharField(max_length=255)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
    ]
