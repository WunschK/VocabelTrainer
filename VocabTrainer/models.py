from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

# Create your models here.
# Welche Modelle machen Sinn?


class AbstractWord(models.Model):
    '''Abstract word model that is the common ground for other words, contains the word_id and the english version of the word
    as an abstract representation of the word.
    '''
    word_id = models.BigAutoField(primary_key=True)
    abstract_word = models.CharField(max_length=100, blank=False, default="", unique=True)

    def __str__(self):
        return f'{self.word_id}, {self.abstract_word}'


class Language(models.Model):
    '''The language(s) that are supported for translations
    '''
    name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f'{self.name}'


class Word(models.Model):
    '''The translated representations of each AbstractWord
    word = the concept behind abstract
    text = the word in the language we are looking for.
    '''
    word = models.ForeignKey(AbstractWord, to_field='abstract_word', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    text = models.CharField(max_length=100, blank=True)
    definition = models.CharField(max_length=100, blank=True)
    learned = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.word}, {self.language}, {self.text}, {self.definition}, {self.learned}'


# Somehow I need to store the words that users already mastered and take them out of the db for that user
class CustomPermission(Permission):
    # Define your custom fields here

    class Meta:
        proxy = True

class CustomGroup(Group):
    # Define your custom fields here

    class Meta:
        proxy = True
class CustomUser(AbstractUser):
    class Meta:
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'

    groups = models.ManyToManyField(
        CustomGroup,
        verbose_name='groups',
        blank=True,
        help_text='The groups this user belongs to.',
        related_name='custom_user_groups'  # Unique related name
    )
    user_permissions = models.ManyToManyField(
        CustomPermission,
        verbose_name='user permissions',
        blank=True,
        help_text='Specific permissions for this user.',
        related_name='custom_user_permissions'  # Unique related name
    )

class UserProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    learned_words = models.ManyToManyField('Word')
