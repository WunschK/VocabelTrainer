import csv
from io import StringIO
import pandas as pd
from .models import AbstractWord, Language, Word

def process_csv_file(csv_file):
    csv_content = csv_file.read().decode('utf-8')
    # Create a DataFrame from the CSV content
    df = pd.read_csv(StringIO(csv_content))

    for _, row in df.iterrows():
        abstract_word, created = AbstractWord.objects.get_or_create(abstract_word=row['Words'])

        language_german = Language.objects.get_or_create(name='German')[0]
        if not Word.objects.filter(word=abstract_word, language=language_german).exists():
            Word.objects.create(word=abstract_word, language=language_german, text=row['German Word'])

        language_indonesian = Language.objects.get_or_create(name='Bahasa Indonesia')[0]
        if not Word.objects.filter(word=abstract_word, language=language_indonesian).exists():
            Word.objects.create(word=abstract_word, language=language_indonesian, text=row['Bahasa Indonesia Word'])


def get_unlearned_words():
    pass



