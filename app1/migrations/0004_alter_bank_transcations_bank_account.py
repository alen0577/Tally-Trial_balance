# Generated by Django 3.2.16 on 2023-03-28 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_bank_transcations_bank_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_transcations',
            name='bank_account',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
