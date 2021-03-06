# Generated by Django 2.0.7 on 2018-07-14 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('time',),
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('speaker', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('events', models.ManyToManyField(to='meetup.Event')),
            ],
            options={
                'ordering': ('create_time',),
            },
        ),
    ]
