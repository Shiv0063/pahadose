# Generated by Django 5.0.7 on 2024-08-05 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_experienceformsa_city_experienceformsa_contactno_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='Category',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
