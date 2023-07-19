from django.contrib import admin
from .models import AbstractWord, Language, Word
# Register your models here.



admin.site.register(AbstractWord)
admin.site.register(Word)
admin.site.register(Language)
