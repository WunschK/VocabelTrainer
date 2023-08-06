from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from .models import AbstractWord, Language, Word
import random
# Create your views here.

class IndexView(TemplateView):
    '''Index View - welcomes the users in the future'''
    template_name= 'VocabTrainer/templates/index.html'


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
        Word_all = Word.objects.all()
        words = Word_all.filter(language__name=language)
        return words
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['words'] = self.get_queryset()
        context['language'] = self.kwargs['language'].lower()
        return context






class WordDetailView(DetailView):
    '''shows the detail of a word users clicked on or that is randomly displayed to them.
    Here a form will appear that users have to enter the meaning of the word.
    '''
    def get(self, request, pk, language):
        word = Word.objects.get(pk=pk)
        language = language
        context = {
            'word' : word,
            'language':language
        }
        return render(request, 'VocabTrainer/templates/word_detail.html', context)
    def post(self, request, pk): # here the language is missing
        word = Word.objects.get(pk=pk)
        user_input = request.POST.get('word_input')
        context = {
            'word' : word,
            'is_submitted': True
        }
        if user_input == word.text:
            context['is_match'] = True
            random_id = random.randint(1, Word.objects.count())
            redirect_url = reverse('word-detail', kwargs={'pk': random_id, 'language': word.language })
            redirect_url_with_param = f'{redirect_url}?refresh={random_id}'

            return redirect(f'{redirect_url_with_param}')
        else:
            context['is_match'] = False

        return render(request, 'VocabTrainer/templates/word_detail.html', context)


# Ich glaube dass ich einen Button "welche Sprache willst du verbessern brauche um auf den entsprechenden Pfad zu kommen,
# dann einfach "language" immer mitschleifen im context und entsprechend auflösen.
# Zumindest mit zwei Sprachen sollte das möglich sein.

