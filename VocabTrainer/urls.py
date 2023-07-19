from VocabTrainer.views import IndexView, LanguageWordListView, WordListView, WordDetailView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('word-list/', WordListView.as_view(), name='word-list-view'),
    path('<str:language>/word-list/', LanguageWordListView.as_view(), name='lang-word-list-view'),
    path('<str:language>/word-list/<int:pk>', WordDetailView.as_view(), name="word-detail"), # later generate one site for each word
    path('word-list/<int:pk>', WordDetailView.as_view(), name="word-detail"), # later generate one site for each word
    ]