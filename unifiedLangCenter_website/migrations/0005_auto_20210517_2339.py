# Generated by Django 2.1.8 on 2021-05-18 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unifiedLangCenter_website', '0004_auto_20210517_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='contents',
            name='about',
            field=models.TextField(default='We are a German teaching and teanslation center in Benin city, Our major area of specialty is to Train you in German and Other languages like spanish,French,Italia,Dutch and Portuguese. Lorem ipsum dolor sit amet consectetur adipisicing elit. Esse amet eum dicta, dolorum quaerat inventore obcaecati error saepe.', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contents',
            name='address',
            field=models.CharField(default='74 Sakponba Road, Benin City Edo State.', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contents',
            name='business_days',
            field=models.CharField(default='Monday - Friday 8am-4pm Saturday, Sunday Closed', max_length=50),
            preserve_default=False,
        ),
    ]