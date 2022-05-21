# Generated by Django 4.0.4 on 2022-05-21 11:50

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0013_alter_message_body_alter_message_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employment',
            fields=[
                ('job_title', models.CharField(blank=True, max_length=200, null=True)),
                ('employer', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.profile')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('degree', models.CharField(blank=True, max_length=200, null=True)),
                ('city', models.CharField(blank=True, max_length=200, null=True)),
                ('school', models.CharField(blank=True, max_length=200, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('description', models.TextField()),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('owner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='resume.profile')),
            ],
        ),
    ]