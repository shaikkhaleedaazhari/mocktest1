# Generated by Django 4.1.3 on 2025-03-06 17:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restoapp', '0010_aregisters_remove_bookers_useremail_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='rbookers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('checkin', models.CharField(max_length=255)),
                ('checkout', models.CharField(max_length=255)),
                ('adult', models.CharField(max_length=255)),
                ('child', models.CharField(max_length=255)),
                ('room', models.CharField(max_length=255)),
                ('specialreq', models.CharField(max_length=255)),
                ('uid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='restoapp.registers')),
            ],
        ),
    ]
