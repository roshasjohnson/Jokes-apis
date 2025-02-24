# Generated by Django 5.1.6 on 2025-02-24 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Joke',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=20)),
                ('joke', models.TextField(blank=True, null=True)),
                ('setup', models.TextField(blank=True, null=True)),
                ('delivery', models.TextField(blank=True, null=True)),
                ('nsfw', models.BooleanField()),
                ('political', models.BooleanField()),
                ('sexist', models.BooleanField()),
                ('safe', models.BooleanField()),
                ('lang', models.CharField(max_length=10)),
            ],
        ),
    ]
