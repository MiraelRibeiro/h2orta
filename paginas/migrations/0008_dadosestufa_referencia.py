# Generated by Django 3.1.2 on 2020-11-30 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0007_remove_dadosestufa_referencia'),
    ]

    operations = [
        migrations.AddField(
            model_name='dadosestufa',
            name='referencia',
            field=models.CharField(blank=True, max_length=2),
        ),
    ]
