# Generated by Django 2.1.2 on 2018-12-08 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PathlabName',
            fields=[
                ('pathlabid', models.AutoField(primary_key=True, serialize=False)),
                ('pathlabname', models.CharField(max_length=30)),
                ('latitude', models.FloatField(max_length=30)),
                ('longitude', models.FloatField(max_length=30)),
            ],
        ),
    ]
