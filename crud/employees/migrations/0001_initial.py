# Generated by Django 3.0.6 on 2020-05-22 02:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('document_number', models.CharField(max_length=20, unique=True)),
                ('birth_date', models.DateField(null=True)),
                ('mobile_number', models.CharField(max_length=40, unique=True)),
                ('email', models.CharField(max_length=100, unique=True)),
                ('gender', models.CharField(max_length=5)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='employees.Department')),
            ],
            options={
                'db_table': 'employee',
            },
        ),
    ]
