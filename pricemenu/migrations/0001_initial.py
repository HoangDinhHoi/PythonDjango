# Generated by Django 2.0.7 on 2018-07-27 03:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PriceMenu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.FloatField(max_length=50)),
                ('pub_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]
