# Generated by Django 5.0.7 on 2024-08-08 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_rename_city_experienceformsa_country_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(blank=True, max_length=255, null=True)),
                ('ContactNo', models.CharField(blank=True, max_length=255, null=True)),
                ('WPNo', models.CharField(blank=True, max_length=255, null=True)),
                ('Email', models.CharField(blank=True, max_length=255, null=True)),
                ('Msg', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.AlterField(
            model_name='experience',
            name='Address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='Category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='Days',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='Description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='Price',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='SmallDescription',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='View',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experiencecategory',
            name='Category',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experiencecategory',
            name='Description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceformsa',
            name='ContactNo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceformsa',
            name='Country',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceformsa',
            name='Countrycode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceformsa',
            name='Email',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceformsa',
            name='Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceformsa',
            name='Pincode',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceformsa',
            name='WPNo',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceformsq',
            name='Name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceincluded',
            name='Lines',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='experienceincluded',
            name='Types',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='FullName',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='userdetails',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
