# Generated by Django 3.2.8 on 2022-08-18 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='modelo',
            name='tags',
        ),
        migrations.AddField(
            model_name='modelo',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='model.Tags'),
        ),
    ]
