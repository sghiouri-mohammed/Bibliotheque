# Generated by Django 4.2.6 on 2024-01-16 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elibrary', '0002_livre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('id_etudiant', models.IntegerField()),
                ('id_livre', models.IntegerField()),
            ],
        ),
    ]
