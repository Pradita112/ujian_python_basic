# Generated by Django 3.2 on 2022-03-19 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='makanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=45)),
                ('asal', models.CharField(max_length=45)),
                ('gambar', models.ImageField(upload_to='makanan')),
            ],
        ),
    ]
