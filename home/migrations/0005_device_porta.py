# Generated by Django 4.0.3 on 2023-10-28 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_device_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='porta',
            field=models.SmallIntegerField(default=0, verbose_name='Porta do ESP32'),
            preserve_default=False,
        ),
    ]
