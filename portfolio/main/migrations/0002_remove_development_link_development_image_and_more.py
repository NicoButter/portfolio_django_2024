# Generated by Django 5.0.7 on 2024-07-21 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="development",
            name="link",
        ),
        migrations.AddField(
            model_name="development",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="developments/"),
        ),
        migrations.AlterField(
            model_name="development",
            name="title",
            field=models.CharField(max_length=100),
        ),
    ]
