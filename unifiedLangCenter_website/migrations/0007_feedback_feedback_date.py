# Generated by Django 2.1.8 on 2021-05-18 11:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('unifiedLangCenter_website', '0006_contents_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='feedback_date',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
