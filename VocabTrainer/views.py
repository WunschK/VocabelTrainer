from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic import TemplateView, ListView, DetailView
from .models import AbstractWord, Language, Word
import random
# Create your views here.

class IndexView(TemplateView):
    def get(self, request):
        return HttpResponse("<h1>Index</h1>")


class WordListView(ListView):
    model = Word
    template_name = 'word_list.html'
    context_object_name = 'words'
    def get_queryset(self):
        words = Word.objects.all()
        return words

# class LanguageWordListView(ListView):
#     def get(self, request, language):
#         words = Word.objects.all().filter(language__name= language)
#         context = {
#             'words': words,
#             'language':language
#
#         }
#         return render(request, 'VocabTrainer/word_list.html', context)




class LanguageWordListView(ListView):
    template_name = 'word_list.html'
    model = Word
    context_object_name = 'words'
    def get_queryset(self, **kwargs):
        words = super().get_queryset(**kwargs)
        return words.filter(language__name = self.kwargs['language'])



class WordDetailView(DetailView):
    def get(self, request, pk):
        word = Word.objects.get(pk=pk)
        context = {
            'word' : word
        }
        return render(request, 'VocabTrainer/word_detail.html', context)
    def post(self, request, pk):
        word = Word.objects.get(pk=pk)
        user_input = request.POST.get('word_input')
        context = {
            'word' : word,
            'is_submitted': True
        }
        if user_input == word.text:
            context['is_match'] = True
            random_id= random.randint(1, Word.objects.count())
            redirect_url = reverse('word-detail', kwargs={'pk': random_id})
            redirect_url_with_param = f'{redirect_url}?refresh={random_id}'

            return redirect(f'{redirect_url_with_param}',)
        else:
            context['is_match'] = False

        return render(request, 'VocabTrainer/word_detail.html', context)


# Ich glaube dass ich einen Button "welche Sprache willst du verbessern brauche um auf den entsprechenden Pfad zu kommen,
# dann einfach "language" immer mitschleifen im context und entsprechend auflösen.
# Zumindest mit zwei Sprachen sollte das möglich sein.

