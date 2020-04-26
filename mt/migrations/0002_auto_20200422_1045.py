# Generated by Django 3.0.3 on 2020-04-22 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestdetail',
            name='desc',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='residentdetail',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='residentdetail',
            name='phone_number',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
