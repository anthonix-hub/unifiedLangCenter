# Generated by Django 2.1.8 on 2021-05-18 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unifiedLangCenter_website', '0008_auto_20210518_0004'),
    ]

    operations = [
        migrations.CreateModel(
            name='pactice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('words_to_translate', models.TextField(max_length=1000)),
            ],
        ),
    ]