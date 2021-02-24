# Generated by Django 3.1.6 on 2021-02-17 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Members',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('div', models.CharField(max_length=1)),
                ('srno', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('role', models.TextField()),
            ],
        ),
    ]
