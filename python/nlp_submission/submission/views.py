#imported necessary functions from all the packages
from django.shortcuts import render
from django.http import HttpResponse
# import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.tag import pos_tag
from nltk.stem import WordNetLemmatizer


# computes pos, statistics and lemmas for every user entered document 
def process_sentence(sentence):
    print(sentence)
    print('=====')
    stop_words = set(stopwords.words('english'))

    tagged_sent_nouns = 0
    tagged_list = []
    lemma_list = []

    sent_list = sent_tokenize(sentence)
    lemmatizer = WordNetLemmatizer()

    for sentence in sent_list:

        word_list = word_tokenize(sentence) #word tokenization
        print(word_list)
        print('=====')


        #stopwords removal
        word_list = [word for word in word_list if not word in stop_words] 


        #parts of speech tagging
        tagged = pos_tag(word_list) 

        # nouns' identification and lemmatization
        for tag in tagged:
            if len(tag[1]) > 1:
                lemma_list.append([tag[0],lemmatizer.lemmatize(tag[0])])
                if tag[1].startswith('NN'):
                    tagged_sent_nouns += 1

        tagged_list.append(tagged)


        print("The entire tagged sentence is",tagged)
        print('=====')

    # list of words and their corresponding lemmas
    lemma_list = [e for e in lemma_list if len(e[1]) > 1]

    solution = {
        'tagged_sentences':tagged_list,
        'total_words_without_stop_words': len(lemma_list),
        'total_nouns': tagged_sent_nouns,
        'total_sentences': len(sent_list),
        'lemmas': lemma_list
    }

    return solution

# renders the index or home page
def index(request):
    return render(request,"submission/frontend.html")

# computes the result for every document and renders the output page
def submission(request):
    sentence = request.POST['sent'].strip()
    processed_sentence = process_sentence(sentence)
    print(processed_sentence)
    return render(request, "submission/output.html", processed_sentence)

