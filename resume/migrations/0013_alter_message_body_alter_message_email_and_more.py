# Generated by Django 4.0.4 on 2022-05-21 10:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0012_alter_profile_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='body',
            field=models.TextField(verbose_name='Your Message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='email',
            field=models.EmailField(blank=True, max_length=200, null=True, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='message',
            name='name',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='message',
            name='subject',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='Subject'),
        ),
    ]
