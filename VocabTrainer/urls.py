from VocabTrainer.views import IndexView, LanguageWordListView, WordListView, WordFormView, LanguageList, RegisterFormView, UserProfileView, UploadCSVView
from django.urls import include,path
from django.conf import settings
from django.conf.urls.static import static
import django.contrib.auth.urls


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('word-list/', WordListView.as_view(), name='word-list-view'),
    path('word-list/<str:language>/', LanguageWordListView.as_view(), name='lang-word-list-view'),
    path('word-list/<str:language>/<int:pk>', WordFormView.as_view(), name='word-form'),
    path('languages', LanguageList.as_view(), name='language-list'),
    path('accounts/signup', RegisterFormView.as_view(), name='register'),
    path('accounts/profile/<int:pk>/', UserProfileView.as_view(), name='profile'),
    path('upload_csv', UploadCSVView.as_view(), name='upload-csv')
    ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Available routes for login
# accounts/ login/ [name='login']
# accounts/ logout/ [name='logout']
# accounts/ password_change/ [name='password_change']
# accounts/ password_change/done/ [name='password_change_done']
# accounts/ password_reset/ [name='password_reset']
# accounts/ password_reset/done/ [name='password_reset_done']
# accounts/ reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/ reset/done/ [name='password_reset_complete']