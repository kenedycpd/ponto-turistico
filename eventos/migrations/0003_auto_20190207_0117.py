# Generated by Django 2.0 on 2019-02-07 01:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventos', '0002_atracao_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atracao',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='img_atracoes'),
        ),
    ]
