# Generated by Django 2.0.7 on 2018-07-28 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0007_auto_20180728_0807'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='menu',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pricemenu.PriceMenu'),
        ),
    ]
