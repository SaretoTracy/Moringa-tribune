# Generated by Django 4.0.3 on 2022-03-24 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0004_article_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='article_image',
            field=models.ImageField(upload_to='articles/'),
        ),
    ]
