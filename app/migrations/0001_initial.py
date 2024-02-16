# Generated by Django 4.2.5 on 2024-02-05 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SoatModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.CharField(max_length=50)),
                ('islike', models.BooleanField(default=True)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
