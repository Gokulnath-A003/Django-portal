# Generated by Django 4.2.1 on 2023-05-22 04:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='csbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Reg', models.CharField(default='', max_length=10)),
                ('Dm', models.PositiveIntegerField()),
                ('Oops', models.PositiveIntegerField()),
                ('Dbms', models.PositiveIntegerField()),
                ('Os', models.PositiveIntegerField()),
                ('Ds', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='faculty',
            fields=[
                ('Name', models.CharField(default='', max_length=20)),
                ('Id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Dept', models.CharField(max_length=20)),
                ('Mobile', models.IntegerField()),
                ('Password', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='student',
            fields=[
                ('Sname', models.CharField(default='', max_length=20)),
                ('Reg', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('Dept', models.CharField(default='', max_length=20)),
                ('Class', models.CharField(default='', max_length=20)),
                ('Psd', models.CharField(default='', max_length=10)),
            ],
        ),
    ]
