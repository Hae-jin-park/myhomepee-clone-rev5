# Generated by Django 4.2.13 on 2024-07-22 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_alter_post_slug"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="post",
            name="slug",
        ),
    ]
