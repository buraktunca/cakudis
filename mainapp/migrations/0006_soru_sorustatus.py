# Generated by Django 3.0.7 on 2020-10-14 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_auto_20201014_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='soru',
            name='sorustatus',
            field=models.CharField(choices=[('Cevaplanmadı', 'Cevaplanmadı'), ('Cevaplandı', 'Cevaplandı')], default='Cevaplanmadı', max_length=200),
        ),
    ]