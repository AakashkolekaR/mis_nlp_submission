import nltk
from nltk.corpus import stopwords
from nltk.corpus.reader import lin
from nltk.tokenize import word_tokenize, sent_tokenize
stop_words = set(stopwords.words('english'))

with open('backend_test.txt') as file:
    lines   =  file.readlines()
    lines = [line.split("\n")[0] for line in lines ]

total_words = 0
total_words_without_stop_words = 0
total_words_with_stop_words = 0
tagged_sent_nouns = 0
tagged_list = []

for line in lines:	
    word_list = nltk.word_tokenize(line)
    # total_words_with_stop_words += len(word_list)

    word_list = [word for word in word_list if not word in stop_words]

    tagged = nltk.pos_tag(word_list)
    for tag in tagged:
        if len(tag[1]) > 1:
            total_words+=1
            if tag[1].startswith('NN'):
                tagged_sent_nouns += 1

    print(tagged)
    tagged_list.append(tagged)


with open('submission_output.txt', 'w') as f:
    print('==========', file=f)
    print("Total no of sentences",len(lines), file=f)
    print('==========', file=f)
    print("Total no of words", total_words, file=f)
    print('==========', file=f)
    print("Total no of nouns", tagged_sent_nouns, file=f)
    print('==========', file=f)
    print("Tagged Sentences are", file=f)
    print('==========', file=f)
    for e in tagged_list:
        print(e, file=f)
        print('==========', file=f)



