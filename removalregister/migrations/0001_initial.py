# Generated by Django 3.2.5 on 2021-07-12 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RemovalReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chittyname', models.CharField(max_length=200)),
                ('chittalName', models.CharField(max_length=200)),
                ('chittalNo', models.IntegerField()),
                ('removalDate', models.CharField(max_length=200)),
                ('time', models.CharField(max_length=200)),
            ],
        ),
    ]
