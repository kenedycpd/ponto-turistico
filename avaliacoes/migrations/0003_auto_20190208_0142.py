# Generated by Django 2.0 on 2019-02-08 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_auto_20190208_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=2, max_digits=7),
        ),
    ]
