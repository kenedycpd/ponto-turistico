# Generated by Django 2.0 on 2019-02-06 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('decricao', models.TextField(verbose_name='Descrição')),
                ('categoria', models.CharField(choices=[('A', 'Adulto'), ('I', 'Infantil'), ('R', 'Religioso')], max_length=1, verbose_name='Categoria')),
            ],
            options={
                'verbose_name': 'Atração',
                'verbose_name_plural': 'Atrações',
            },
        ),
    ]
