# Generated by Django 4.0.4 on 2022-05-31 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('codesimple', '0007_comment_created_by_alter_comment_blogpost'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post_id',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]