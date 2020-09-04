# Generated by Django 3.0.8 on 2020-09-02 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Department', models.CharField(choices=[('ece', 'ECE'), ('cse', 'CSE'), ('it', 'IT'), ('me', 'Mech'), ('ce', 'Civil')], max_length=10)),
                ('Qualification', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
