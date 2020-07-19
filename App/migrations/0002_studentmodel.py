# Generated by Django 2.2.12 on 2020-07-12 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('contact', models.IntegerField(unique=True)),
                ('email', models.EmailField(max_length=30, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
