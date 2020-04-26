# Generated by Django 3.0.2 on 2020-04-01 14:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catID', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_id', models.CharField(max_length=200)),
                ('subject', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=500)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UnitDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unitID', models.PositiveIntegerField()),
                ('aptNo', models.PositiveIntegerField()),
                ('street', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zipcode', models.PositiveIntegerField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResidentDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.DateField(blank=True, max_length=100, null=True)),
                ('vehNumber', models.CharField(blank=True, max_length=100, null=True)),
                ('is_Primary', models.CharField(blank=True, choices=[('yes', 'YES'), ('no', 'NO')], default='no', max_length=200, null=True)),
                ('phone_number', models.PositiveIntegerField(blank=True, null=True)),
                ('moveInDate', models.DateField(blank=True, max_length=100, null=True)),
                ('moveOutDate', models.DateField(blank=True, max_length=100, null=True)),
                ('rent', models.PositiveIntegerField(blank=True, null=True)),
                ('occupation', models.CharField(blank=True, max_length=200, null=True)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('modifiedBy', models.CharField(blank=True, max_length=200, null=True)),
                ('unitID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='units', to='mt.UnitDetail')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='RequestDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('priority', models.CharField(choices=[('standard', 'STANDARD'), ('urgent', 'URGENT')], default='standard', max_length=50)),
                ('status', models.CharField(blank=True, choices=[('new', 'NEW'), ('in-progress', 'IN-PROGRESS'), ('completed', 'COMPLETED')], max_length=100, null=True)),
                ('accessInstructions', models.CharField(blank=True, max_length=200, null=True)),
                ('perToEnter', models.CharField(choices=[('yes', 'YES'), ('no', 'NO')], default='no', max_length=50)),
                ('created_date', models.DateField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('modifiedBy', models.CharField(blank=True, max_length=200, null=True)),
                ('type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='categories', to='mt.Category')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='residents', to='mt.ResidentDetail')),
            ],
        ),
    ]