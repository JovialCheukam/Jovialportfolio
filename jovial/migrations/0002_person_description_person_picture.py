# Generated by Django 5.1.4 on 2024-12-14 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jovial", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="person",
            name="description",
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name="person",
            name="picture",
            field=models.ImageField(blank=True, null=True, upload_to="profile/"),
        ),
    ]
