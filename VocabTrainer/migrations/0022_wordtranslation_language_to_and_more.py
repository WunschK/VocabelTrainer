# Generated by Django 4.2.3 on 2023-07-14 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VocabTrainer', '0021_remove_wordtranslation_translation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='wordtranslation',
            name='language_to',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='VocabTrainer.language'),
        ),
        migrations.AlterField(
            model_name='wordtranslation',
            name='translation',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterUniqueTogether(
            name='wordtranslation',
            unique_together={('vocabulary', 'language_to', 'translation')},
        ),
    ]
