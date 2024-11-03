# Generated by Django 5.0.7 on 2024-11-03 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0008_categorymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]