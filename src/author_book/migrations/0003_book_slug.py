# Generated by Django 4.1.7 on 2023-03-31 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('author_book', '0002_alter_author_firstname_alter_author_secondname_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]