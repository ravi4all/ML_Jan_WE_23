import spacy
from spacy.lang.en.stop_words import STOP_WORDS
import string
from heapq import nlargest

def generate(text):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    document = nlp(text)
    tokens =[token.text for token in document]
    punctuation = string.punctuation + '\n'
    word_frequencies = {}
    for word in document:
        if word.text.lower() not in stopwords:
            if word.text.lower() not in punctuation:
                if word.text not in word_frequencies.keys():
                    word_frequencies[word.text] = 1
                else:
                    word_frequencies[word.text] += 1

    max_frequency = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = word_frequencies[word] / max_frequency

    sentence_tokens = [sent for sent in document.sents]

    sentence_scores = {}
    for sent in sentence_tokens:
        for word in sent:
            if word.text.lower() in word_frequencies.keys():
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()] 
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]

    select_length = int(len(sentence_tokens)*0.3)
    summary = nlargest(select_length,sentence_scores,key = sentence_scores.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)

    return summary