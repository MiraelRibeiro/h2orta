# Generated by Django 3.1.2 on 2020-11-30 18:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0004_dadosestufa_referencia'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dadosestufa',
            name='referencia',
        ),
    ]
