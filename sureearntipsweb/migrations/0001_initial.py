# Generated by Django 3.1.7 on 2021-10-13 13:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Predictions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teama_odds', models.DecimalField(decimal_places=2, max_digits=5)),
                ('teamb_odds', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description_predictions', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teamname', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Fixtures',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('fieldvenue', models.CharField(max_length=20)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sureearntipsweb.teams')),
            ],
        ),
    ]
