# Generated by Django 4.0.4 on 2022-05-22 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0017_alter_education_end_date_alter_education_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employment',
            name='end_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='employment',
            name='start_date',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
