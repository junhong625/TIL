# Generated by Django 3.2.13 on 2022-11-17 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_survey_category_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='style',
            field=models.ManyToManyField(related_name='same_style_user', through='accounts.Survey', to='accounts.Survey_category'),
        ),
    ]