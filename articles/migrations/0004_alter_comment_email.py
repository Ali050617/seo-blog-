# Generated by Django 5.1.4 on 2025-01-09 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_author_alter_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
