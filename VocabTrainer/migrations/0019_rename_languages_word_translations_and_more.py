# Generated by Django 4.2.3 on 2023-07-14 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VocabTrainer', '0018_word_word'),
    ]

    operations = [
        migrations.RenameField(
            model_name='word',
            old_name='languages',
            new_name='translations',
        ),
        migrations.AddField(
            model_name='wordphrase',
            name='word_indo',
            field=models.CharField(default='', max_length=50),
        ),
    ]
