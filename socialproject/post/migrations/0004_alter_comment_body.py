# Generated by Django 4.2.5 on 2023-10-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0003_comment"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="body",
            field=models.CharField(max_length=100),
        ),
    ]
