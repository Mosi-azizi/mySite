# Generated by Django 4.0.4 on 2022-06-06 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0027_welcome_email_remove_message_welcome_message_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='welcome_email',
        ),
    ]
