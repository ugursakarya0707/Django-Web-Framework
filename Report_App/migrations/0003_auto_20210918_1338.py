# Generated by Django 2.2.5 on 2021-09-18 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0002_auto_20210917_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='intro',
            field=models.TextField(default=''),
        ),
    ]
