# Generated by Django 2.2.6 on 2019-10-21 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0003_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
