# Generated by Django 2.1.8 on 2021-05-18 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unifiedLangCenter_website', '0009_pactice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='business_days',
            field=models.TextField(max_length=50),
        ),
    ]
