# OXIDO - Zadanie Rekrutacyjne

### Wymagane biblioteki

- OpenAI API

  `pip install openai`
- DotEnv

  `pip install dotenv`

### Instrukcja uruchomienia

1. Do głównego folderu dodaj plik tekstowy "Zadanie dla JJunior AI Developera - tresc artykulu.txt" na podstawie, którego będzie generowana
   zawartość HTML.
2. Dodaj plik .env do głównego folderu z kluczami jak pokazano poniżej

```
API_KEY='$TWÓJ_KLUCZ_OPENAI_API'
ORG='$ID_ORGANIZACJI'
PROJECT_ID='$ID_PROJEKTU'
```

3. Uruchom plik main.py.
4. Gotowe

### Opis działania programu

Program na początku wczytuje dane podane w pliku "Zadanie dla JJunior AI Developera - tresc artykulu.txt", a
następnie wysła odpowiednie zapytanie do AI wykorzystując biblioteke OpenAI API.
Wygenerowana odpowiedź zostaje zapisana do pliku "artykul.html". Aplikacja posiada obsługę ewentualnych
wyjątków jakie mogą pojawić się podczas całego procesu aplikacji, jak również odpowiednie komunikaty przedstawiające
przebieg pracy aplikacji. Został również stworzony szablon oraz pogląd
prostej strony HTML wykorzystując zasoby CSS.

