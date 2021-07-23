from django.shortcuts import render
from django.http import HttpResponse
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize


def process_sentence(sentence):
    print(sentence)
    print('=====')
    stop_words = set(stopwords.words('english'))

    total_words = 0
    total_words_without_stop_words = 0
    total_words_with_stop_words = 0
    tagged_sent_nouns = 0
    tagged_list = []

    sent_list = nltk.sent_tokenize(sentence)

    for sentence in sent_list:
        word_list = nltk.word_tokenize(sentence) #word tokenization
        print(word_list)
        print('=====')
        # total_words_with_stop_words += len(word_list)

        word_list = [word for word in word_list if not word in stop_words] #removing stop words
        #total_words_without_stop_words += total_words_with_stop_words - len(word_list)

        tagged = nltk.pos_tag(word_list) #parts of speech tagging
        for tag in tagged:
            if len(tag[1]) > 1:
                total_words+=1
                if tag[1].startswith('NN'):
                    tagged_sent_nouns += 1

        tagged_list.append(tagged)
        print("The entire tagged sentence is",tagged)
        print('=====')

    print("Total no of words without stopwords", total_words)
    print("Total no of nouns", tagged_sent_nouns)

    solution = {
        'tagged_sentences':tagged_list,
        'total_words_without_stop_words': total_words,
        'total_nouns': tagged_sent_nouns,
        'total_sentences': len(sent_list)
    }

    return solution

def index(request):
    return render(request,"submission/frontend.html")
    
def submission(request):
    sentence = request.POST['sent'].strip()
    processed_sentence = process_sentence(sentence)
    print(processed_sentence)
    return render(request, "submission/output.html", processed_sentence)

