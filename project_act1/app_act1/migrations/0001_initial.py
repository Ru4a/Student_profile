# Generated by Django 4.2.1 on 2023-05-26 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('grade', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'student_info',
                'managed': False,
            },
        ),
    ]
