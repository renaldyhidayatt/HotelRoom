# Generated by Django 2.2.10 on 2020-03-29 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('title', models.CharField(max_length=15)),
                ('image', models.ImageField(upload_to='agents/')),
            ],
        ),
    ]
