# Generated by Django 3.1.5 on 2021-06-28 16:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='tags',
        ),
        migrations.DeleteModel(
            name='Tags',
        ),
    ]
