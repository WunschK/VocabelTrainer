# Generated by Django 4.2.3 on 2023-07-13 14:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('VocabTrainer', '0003_alter_wordtranslation_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='wordtranslation',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='wordtranslation',
            name='language_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='VocabTrainer.language'),
        ),
        migrations.AlterUniqueTogether(
            name='wordtranslation',
            unique_together={('vocabulary', 'language_to', 'translation')},
        ),
        migrations.RemoveField(
            model_name='wordtranslation',
            name='language',
        ),
    ]
