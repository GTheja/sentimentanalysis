# take data from read.tex
# encoding is used because most of text in the webiste in form utf-encoding thats why we use encoding
import string
from collections import Counter
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
#corups is dataset
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import matplotlib.pyplot as plt
text = open('read.txt', encoding='utf-8').read()
lower_case = text.lower()

# str1: specifies the list of characters that need to be replaced
# str1: specifies the list of characters with which the characters need to be replaced
# str1: specifies the list of characters that need to be deleted

# str1 = 'abc' replaced by str2
# str2 = 'gef'

cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))
# nlp is analysis of words not sentence thats why tokenization is important.

#word_tokenize: if text becomes big text or book take less time to run
tokenized_words = word_tokenize(cleaned_text, "english")


# stop words which don't add any meaning to scentence
# removing stop_words improve analise timming.


final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

lemma_words = []
for word in final_words:
    word = WordNetLemmatizer().lemmatize(word)
    lemma_words.append(word)

emotion_list =[]
with open('emotions.txt', 'r') as file:
    for line in file:
        clear_line = line.replace('\n', '').replace(',', '').replace("'", '').strip()
        word, emotion = clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)
print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    if score['neg'] > score['pos']:
        print("Negative Sentiment")
    elif score['neg'] < score['pos']:
        print("Positive Sentiment")
    else:
        print("Neutral Sentiment")

sentiment_analyse(cleaned_text)


fig, ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()


