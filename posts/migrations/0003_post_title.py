# Generated by Django 3.2.10 on 2022-03-05 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='post', max_length=255),
            preserve_default=False,
        ),
    ]
