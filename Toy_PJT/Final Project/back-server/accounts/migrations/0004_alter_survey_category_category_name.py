# Generated by Django 3.2.13 on 2022-11-17 01:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_survey_survey_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey_category',
            name='category_name',
            field=models.CharField(max_length=20),
        ),
    ]
