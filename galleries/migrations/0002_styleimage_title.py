# Generated by Django 2.0.7 on 2018-07-24 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galleries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='styleimage',
            name='title',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
