# Generated by Django 5.1.4 on 2024-12-22 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("jovial", "0006_remove_home_picture_alter_home_greeting"),
    ]

    operations = [
        migrations.AlterField(
            model_name="home",
            name="greeting",
            field=models.CharField(max_length=16),
        ),
    ]
