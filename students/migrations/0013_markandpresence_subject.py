# Generated by Django 3.0.2 on 2020-01-13 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0012_auto_20191231_0928'),
    ]

    operations = [
        migrations.AddField(
            model_name='markandpresence',
            name='subject',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
