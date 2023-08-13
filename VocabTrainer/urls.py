from VocabTrainer.views import IndexView, LanguageWordListView, WordListView, WordFormView
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('word-list/', WordListView.as_view(), name='word-list-view'),
    path('word-list/<str:language>/', LanguageWordListView.as_view(), name='lang-word-list-view'),
    path('word-list/<str:language>/<int:pk>', WordFormView.as_view(), name='word-form'),
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)