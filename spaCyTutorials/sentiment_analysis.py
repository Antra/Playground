import spacy
import pandas as pd
from spacy.lang.en.stop_words import STOP_WORDS
import string
from spacy.lang.en import English

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

nlp = spacy.load('en_core_web_sm')

# Text classification -- sentiment analysis
# dataset source: http://archive.ics.uci.edu/ml/datasets/Sentiment+Labelled+Sentences
df_yelp = pd.read_table('sentiments/yelp_labelled.txt')
df_imdb = pd.read_table('sentiments/imdb_labelled.txt')
df_amz = pd.read_table('sentiments/amazon_cells_labelled.txt')

# concatenate the datasets
frames = [df_yelp, df_imdb, df_amz]

# then fix the column headers (no header in input)
for colname in frames:
    colname.columns = ["Message", "Target"]

# Assigning a key to make it easier
keys = ['Yelp', 'IMDB', 'Amazon']
# then merge/concat the datasets
df = pd.concat(frames, keys=keys)
print(df.shape)
print(df.head(5))
df.to_csv('sentiments/sentimentdataset1.csv')

# clean-up exercise - columns ok?
print(df.columns)
# and any missing values?
print(df.isnull().sum())

# build a list of stopwords to use for filtering
stopwords = list(STOP_WORDS)

# Okay, let's get a text ready and start processing
ex16 = nlp(
    u"This is how John Walker was walking. He was also running beside the lawn.")

for word in ex16:
    print(word.text, "Lemma =>", word.lemma_)

# Okay, the pronouns (e.g. 'He') have lemma -PRON-, so we can filter them out
for word in ex16:
    if word.lemma_ != '-PRON-':
        print(word.lemma_.lower().strip())

# Build a list comprehension -- essentially take the above, start from the back and fill it out (and put the actual pronouns in instead of their lemmas)
sentiment_list = [word.lemma_.lower().strip() if word.lemma_ !=
                  '-PRON-' else word.lower_ for word in ex16]

# filtering out stopwords and punctuations
for word in ex16:
    if word.is_stop == False and not word.is_punct:
        print(word)

# and again as list comprehension
sentiment_list = [word for word in ex16 if word.is_stop ==
                  False and not word.is_punct]
print(sentiment_list)


# A better way is to use the punctuation of the string module -- and to create a special spaCy parser
punctuations = string.punctuation
# 'English()' (or rather spacy.lang.en) is a basic English model containing tokenisation rules, stopwords and lemmatisation tables
# where as 'en_core_web_sm' is a statistical model which includes language data and binary weights to make predictions about POS, dependencies and NER
parser = English()


def spacy_tokeniser(sentence):
    mytokens = parser(sentence)
    mytokens = [word.lemma_.lower().strip() if word.lemma_ !=
                '-PRON-' else word.lower_ for word in mytokens]
    mytokens = [
        word for word in mytokens if word not in stopwords and word not in punctuations]
    return mytokens


# Custom transformer using spaCy
class predictors(TransformerMixin):
    def transform(self, X, **transform_params):
        return [clean_text(text) for text in X]

    def fit(self, X, y=None, **fit_params):
        return self

    def get_params(self, deep=True):
        return {}


# Basic function to clean the text
def clean_text(text):
    return text.strip().lower()


# Vectorisation
vectoriser = CountVectorizer(tokenizer=spacy_tokeniser, ngram_range=(1, 1))
classifier = LinearSVC()

# Using Tfidf
tfvectoriser = TfidfVectorizer(tokenizer=spacy_tokeniser)

# Features and labels
X = df['Message']
ylabels = df['Target']

X_train, X_test, y_train, y_test = train_test_split(
    X, ylabels, test_size=0.2, random_state=42)

# Create the pipeline to clean, tokenise, vectorise, and classify
pipe = Pipeline([("cleaner", predictors()),
                 ('vectoriser', vectoriser),
                 ('classifier', classifier)])

# Fit our data
pipe.fit(X_train, y_train)

# Predicting with a test dataset
sample_prediction = pipe.predict(X_test)

# Prediction Results
# 1 = Positive review
# 0 = Negative review
for (example, pred) in zip(X_test, sample_prediction):
    print(example, "Prediction =>", pred)
# Accuracy
print("Accuracy: ", pipe.score(X_test, y_test))
print("Accuracy: ", pipe.score(X_test, sample_prediction))

# Another random review
t1 = pipe.predict(["This was a great movie!"])
t2 = pipe.predict(["I do enjoy my job",
                   "What a poor product!, I will have to get a new one", "I feel amazing!"])
print(t1, t2)
