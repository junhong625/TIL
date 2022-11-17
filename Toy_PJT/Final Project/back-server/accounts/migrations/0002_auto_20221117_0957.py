# Generated by Django 3.2.13 on 2022-11-17 00:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(blank=True)),
                ('price', models.IntegerField(blank=True)),
                ('status', models.IntegerField()),
                ('expiration_date', models.DateField(blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='membership',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.membership'),
        ),
    ]
