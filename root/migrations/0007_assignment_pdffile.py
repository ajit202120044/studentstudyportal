# Generated by Django 3.2.8 on 2022-04-19 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('root', '0006_assignment_marks'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='pdffile',
            field=models.FileField(default=None, max_length=250, null=True, upload_to='assign/'),
        ),
    ]