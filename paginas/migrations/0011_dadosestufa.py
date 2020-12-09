# Generated by Django 3.1.2 on 2020-11-30 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paginas', '0010_delete_dadosestufa'),
    ]

    operations = [
        migrations.CreateModel(
            name='DadosEstufa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(blank=True, max_length=50)),
                ('valor', models.CharField(blank=True, max_length=50)),
                ('slots', models.CharField(blank=True, max_length=2)),
                ('fileiras', models.CharField(blank=True, max_length=2)),
                ('itensInclusos', models.CharField(blank=True, max_length=255)),
                ('bombaAgua', models.BooleanField()),
                ('tamanhoCM', models.CharField(blank=True, max_length=10)),
                ('estrutura', models.CharField(blank=True, max_length=20)),
                ('imagem', models.CharField(blank=True, max_length=255)),
                ('referencia', models.CharField(blank=True, max_length=2)),
            ],
            options={
                'db_table': 'dados_estufa',
            },
        ),
    ]
