# Generated by Django 5.0.1 on 2024-05-02 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="contenttable",
            name="content_img",
            field=models.ImageField(null=True, upload_to="uploads/Post"),
        ),
    ]