import spacy

# Словник для перетворення тегів spaCy в українські назви
POS_NAMES = {
    "NOUN": "іменник",
    "VERB": "дієслово",
    "ADJ": "прикметник",
    "ADV": "прислівник",
    "PRON": "займенник",
    "PROPN": "прийменник",
    "DET": "займенник",
    "ADP": "прийменник",
    "NUM": "числівник",
    "CONJ": "сполучник",
    "CCONJ": "сполучник",
    "SCONJ": "сполучник",
    "PUNCT": "розділовий_знак",
    "PART": "частка",
    "X": "інше",
    "SYM": "символ",
    "INTJ": "вигук",
}

# Функція для завантаження моделі spaCy
def load_spacy_model():
    nlp = spacy.load("uk_core_news_sm")
    return nlp

# Функція для аналізу та заміни слів на частини мови
def replace_words_with_pos(text, nlp=None):
    if nlp is None:
        nlp = load_spacy_model()
    
    doc = nlp(text)
    
    result = []
    for token in doc:
        if token.is_punct:
            # Зберігаємо пунктуацію як є
            result.append(token.text)
        else:
            # Замінюємо слово на відповідну частину мови
            result.append(POS_NAMES.get(token.pos_, token.pos_))
    
    output = " ".join(result)

    return output
    