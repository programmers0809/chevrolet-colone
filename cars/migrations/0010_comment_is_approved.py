# Generated by Django 5.0.7 on 2024-11-03 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0009_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
