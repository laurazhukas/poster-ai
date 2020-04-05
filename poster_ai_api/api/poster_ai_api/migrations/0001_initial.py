# Generated by Django 2.1.7 on 2019-02-17 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Face',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('face_id', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('anger', models.DecimalField(decimal_places=12, max_digits=13)),
                ('contempt', models.DecimalField(decimal_places=12, max_digits=13)),
                ('disgust', models.DecimalField(decimal_places=12, max_digits=13)),
                ('fear', models.DecimalField(decimal_places=12, max_digits=13)),
                ('happiness', models.DecimalField(decimal_places=12, max_digits=13)),
                ('neutral', models.DecimalField(decimal_places=12, max_digits=13)),
                ('sadness', models.DecimalField(decimal_places=12, max_digits=13)),
                ('surprise', models.DecimalField(decimal_places=12, max_digits=13)),
                ('poster_name', models.CharField(max_length=100)),
                ('poster_id', models.CharField(max_length=100)),
                ('session_id', models.CharField(max_length=100)),
                ('image_uri', models.CharField(max_length=300)),
            ],
        ),
    ]