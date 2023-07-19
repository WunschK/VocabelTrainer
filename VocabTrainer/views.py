from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import AbstractWord, Language, Word
# Create your views here.

class IndexView(TemplateView):
    def get(self, request):
        return HttpResponse("<h1>Index</h1>")


class WordListView(ListView):
    def get(self, request):
        words = Word.objects.all()
        return render(request, 'vocabtrainer/word_list.html', {'words':words})

class LanguageWordListView(ListView):
    def get(self, request, language):
        WP = Word.objects.get(language=language)
        words_language = WP.values()
        return render(request, 'vocabtrainer/word_list.html', {'words':words_language})


class WordDetailView(DetailView):
    def get(self, request, pk):
        word = Word.objects.get(pk=pk)
        context = {
            'word' : word
        }
        return render(request, 'vocabtrainer/word_detail.html', context)
    def post(self, request, pk):
        word = Word.objects.get(pk=pk)
        user_input = request.POST.get('word_input')
        context = {
            'word' : word,
            'is_submitted': True
        }
        if user_input == word.text:
            context['is_match'] = True
        else:
            context['is_match'] = False

        return render(request, 'vocabtrainer/word_detail.html', context)


# Ich glaube dass ich einen Button "welche Sprache willst du verbessern brauche um auf den entsprechenden Pfad zu kommen,
# dann einfach "language" immer mitschleifen im context und entsprechend auflösen.
# Zumindest mit zwei Sprachen sollte das möglich sein.

