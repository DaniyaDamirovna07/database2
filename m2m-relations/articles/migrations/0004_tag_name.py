# Generated by Django 3.2.20 on 2023-08-10 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_alter_article_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
