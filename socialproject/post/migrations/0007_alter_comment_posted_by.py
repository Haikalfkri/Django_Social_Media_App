# Generated by Django 4.2.5 on 2023-10-18 11:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0006_alter_comment_posted_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="posted_by",
            field=models.CharField(max_length=100),
        ),
    ]