# Generated by Django 2.2.2 on 2019-12-26 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('models', '0019_publications_file_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='publications',
            name='urgent',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]
