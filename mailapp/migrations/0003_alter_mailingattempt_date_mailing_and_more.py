# Generated by Django 5.1.5 on 2025-02-15 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mailapp", "0002_alter_mailing_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailingattempt",
            name="date_mailing",
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name="mailingattempt",
            name="mail_server_response",
            field=models.TextField(blank=True, null=True),
        ),
    ]
