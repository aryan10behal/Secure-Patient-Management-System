# Generated by Django 4.0.3 on 2022-11-28 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient_mgmt_backend', '0002_alter_sharerecords_filehash_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendingdocumentrequests',
            name='requestCompleted',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]