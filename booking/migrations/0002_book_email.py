# Generated by Django 2.0.7 on 2018-07-24 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='email',
            field=models.EmailField(max_length=75, null=True),
        ),
    ]
