# Generated by Django 4.0.4 on 2023-04-17 19:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='criador',
        ),
    ]
