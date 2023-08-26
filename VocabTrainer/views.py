from django.shortcuts import render, redirect, get_list_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView
from .forms import AnswerWord
from .models import AbstractWord, Language, Word
import random
# Create your views here.

class IndexView(TemplateView):
    '''Index View - welcomes the users in the future'''
    template_name= 'VocabTrainer/templates/index.html'


# Do I really need the WordListView?
class WordListView(ListView):
    '''list of all words in the database - mainly a intermediate step so that I can check functionality.
    will probably defunct for good, as this view is not really relevant. But was a nice entry point
    '''
    model = Word
    template_name = 'VocabTrainer/templates/word_list.html'
    context_object_name = 'words'

    def get_queryset(self):
        words = Word.objects.all()
        return words


class LanguageWordListView(ListView):
    '''users will pick a language later on and get a filtered list of elements which they can click'''
    template_name = 'VocabTrainer/templates/word_list.html'
    model = Word
    def get_queryset(self):
        language = self.kwargs['language'].lower()
        return Word.objects.filter(language__name__iexact= language)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = self.get_queryset()
        context['language'] = self.kwargs['language'].lower()
        return context


class WordFormView(FormView):
    '''shows the form to enter the meaning of the word.
    Forwards to a random new word, once the word is answered correctly.
    After three incorrect guesses, the word should be skipped
    Todo 1: Implement logic for wrong answers
    '''
    template_name = 'VocabTrainer/templates/word_form.html'
    form_class = AnswerWord
    success_url = None



    def get_context_data(self, **kwargs):
        '''set the context data accordingly - now we can use the current_word in word_form'''
        context = super().get_context_data(**kwargs)
        word_id = self.kwargs.get('pk')
        context['current_word'] = Word.objects.get(pk=word_id)
        return context


    def form_valid(self, form):
        '''checks whether the form is valid'''
        # user_input defines that the field is the form field 'translation'
        user_input = form.cleaned_data['translation']
        # here we pass the current word from get_context_data into this function
        current_word = self.get_context_data()['current_word']
        # save the current word language in a variable current language
        current_language = current_word.language
        if user_input == current_word.text:
            # if the user input is the correct value, forward to a random word:
            # filter Word by the language line that we are in
            language_words = Word.objects.filter(language=current_language)
            # remove the current_word.pk so that the next word will not be the same
            all_language_words_except_current = language_words.exclude(pk=current_word.pk)
            # Todo 2: Implement a list with "learned words" and put the current word if answered correctly to "learned
            #  words" and remove it from the word-list
            #  maybe user handling first with users having their own list of "known words and unknown words
            if all_language_words_except_current.exists():
                random_word = random.choice(all_language_words_except_current)
                self.success_url = reverse('word-form', kwargs={'language':current_language, 'pk':random_word.pk})
            else:
                return self.render_to_response(self.get_context_data(form=self.form_class()))
                # I don't like that I'm repeating myself here
        else:
             return self.render_to_response(self.get_context_data(form=self.form_class()))
        return super().form_valid(form)




