# Generated by Django 3.2.8 on 2022-08-18 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0005_auto_20220818_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelo',
            name='tags',
            field=models.ManyToManyField(blank=True, to='model.Tags'),
        ),
    ]
