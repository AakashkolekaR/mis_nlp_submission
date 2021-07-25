import nltk
from nltk.corpus import stopwords
from nltk.corpus.reader import lin
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.stem import WordNetLemmatizer
stop_words = set(stopwords.words('english'))

input_file = 'backend_test.txt'

with open(input_file) as file:
    lines   =  file.readlines()
    lines = [line.split("\n")[0] for line in lines ]

total_words = 0
total_words_without_stop_words = 0
total_words_with_stop_words = 0
tagged_sent_nouns = 0
tagged_list = []
lemma_list = []

lemmatizer = WordNetLemmatizer()

for line in lines:	
    word_list = nltk.word_tokenize(line)
    # total_words_with_stop_words += len(word_list)

    word_list = [word for word in word_list if not word in stop_words]

    tagged = nltk.pos_tag(word_list)
    for tag in tagged:
        if len(tag[1]) > 1:
            total_words+=1
            lemma_list.append([tag[0],lemmatizer.lemmatize(tag[0])])
            if tag[1].startswith('NN'):
                tagged_sent_nouns += 1

    tagged_list.append(tagged)


with open('submission_output.txt', 'w') as f:
    print('==========', file=f)
    print("Total no of sentences are",len(lines), file=f)
    print('==========', file=f)
    print("Total no of words without stop words are", total_words, file=f)
    print('==========', file=f)
    print("Total no of nouns are", tagged_sent_nouns, file=f)
    print('==========', file=f)
    print("Tagged Sentences are", file=f)
    print('==========', file=f)

    for e in tagged_list:
        print(e, file=f)
        print('==========', file=f)

    print("Lemma for each word is as follows", file=f, end='\n\n')
    for lemma in lemma_list:
        print(lemma[0],lemma[1], file=f, sep="  --------->  ")




