# Generated by Django 3.2.13 on 2022-11-17 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poster_path', models.CharField(max_length=100)),
                ('backdrop_path', models.CharField(max_length=100)),
                ('original_title', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=30)),
                ('original_language', models.CharField(max_length=20)),
                ('runtime', models.IntegerField()),
                ('revenue', models.IntegerField()),
                ('budget', models.IntegerField()),
                ('vote_count', models.IntegerField()),
                ('adult', models.IntegerField()),
                ('movie_id', models.IntegerField()),
                ('vote_average', models.FloatField()),
                ('popularity', models.FloatField()),
                ('release_date', models.DateField()),
                ('overview', models.TextField()),
            ],
        ),
    ]