# Generated by Django 4.0.5 on 2022-08-14 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_article_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='main_image',
            field=models.ImageField(blank=True, upload_to='article_image/'),
        ),
    ]
