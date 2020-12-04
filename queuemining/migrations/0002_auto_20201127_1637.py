# Generated by Django 3.0.3 on 2020-11-27 15:37

from django.db import migrations, models
import queuemining.validator


class Migration(migrations.Migration):

    dependencies = [
        ('queuemining', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.AlterField(
            model_name='document',
            name='document',
            field=models.FileField(upload_to='documents/', validators=[queuemining.validator.validate_file_extension]),
        ),
    ]