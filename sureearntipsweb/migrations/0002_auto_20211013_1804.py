# Generated by Django 3.1.7 on 2021-10-13 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sureearntipsweb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscribers',
            name='id',
        ),
        migrations.AlterField(
            model_name='fixtures',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sureearntipsweb.teams'),
        ),
        migrations.AlterField(
            model_name='predictions',
            name='description_predictions',
            field=models.TextField(max_length=50),
        ),
        migrations.AlterField(
            model_name='subscribers',
            name='phone',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]