# Generated by Django 2.2.6 on 2019-10-19 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rec', '0002_auto_20191019_0523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.TextField()),
                ('message', models.TextField()),
            ],
        ),
    ]
