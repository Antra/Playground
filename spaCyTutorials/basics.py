import spacy
from spacy import displacy
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from spacy.lang.en.stop_words import STOP_WORDS
import string
from spacy.lang.en import English

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.metrics import accuracy_score
from sklearn.base import TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

# download spacy model first, e.g. python -m spacy download <model>
# see available models on https://spacy.io/usage/models
# for multi-language support set language to 'xx'

# same as nlp = spacy.load('en') if linking works
nlp = spacy.load('en_core_web_sm')
# nlp = spacy.load('en_core_web_md')
# nlp = spacy.load('en_core_web_lg')

# Reading a text
docx = nlp(u"SpaCy is an amazing tool like nltk - über nice!")
# print(docx)

# Reading a file
my_file = open("exampletext.txt").read()
doc_file = nlp(my_file)
# print(doc_file)

# Tokenisation: splitting into sentences
for num, sentence in enumerate(doc_file.sents):
    print(f'{num}: {sentence}')

# Tokenisation: splitting into words -- similar to splitting on spaces (e.g. doc_file.text.split(" ")).
for token in doc_file:
    print(token.text)
# or the words returned as a list
list_words = [token.text for token in doc_file]
print(list_words)


# Shapes (capital/upper/lower case, etc.) - '.shape' gives a numeric value, '.shape_' gives a graphical representation
# and the functions .is_alpha and .is_stop
for word in docx:
    print(word.text, word.shape_)


# Part of Speech (POS) tagging - '.pos_' exposes Google Universal pos_tag, (simple) - '.tag_' exposes the Treebank (detailed), useful for training own model
ex1 = nlp("He drinks a drink")
for word in ex1:
    print(word.text, word.pos, word.pos_)

ex2 = nlp("I fish a fish")
for word in ex2:
    print(word.text, word.pos, word.pos_, word.tag_)

# Use spacy.explain as a look-up mechanism, e.g. what is the "VBP" covering?
print(spacy.explain('VBP'))


# More complex sentence; the first is a modifier while the second 'had' is the main verb of the sentence.
ex3 = nlp(
    u"All the faith that he had had had had no effect on the outcome of his life.")

for word in ex3:
    print((word.text, word.tag_, word.pos_))

# Display the graphical representation of the sentence (and the relationship) - will open on http://localhost:5000
# for Jupyter use: displacy.render(ex3, style='dep', jupyter=True)
# displacy.serve(ex3, style='dep')


# Lemmatisation is used for text normalisation; lemmatisation is similar to but a bit different from stemming (which just removes prefix/suffix of a word) as it also gives meaning
docx_lemma = nlp("study studying studious studio student")
for word in docx_lemma:
    print(word.text, word.lemma, word.lemma_, word.pos_)

docx_lemma2 = nlp("Walking walks walk walker")
for word in docx_lemma2:
    print(word.text, word.lemma, word.lemma_, word.pos_)

docx_lemma3 = nlp("good goods run running runner runny was be were")
for word in docx_lemma3:
    print(word.text, word.lemma, word.lemma_, word.pos_)


# Named Entity Recognition (NER) tries to classify a text into predefined categories or 'real-world' object entities (e.g. person, places, organisation)
# For extraction, use: '.ents' (list of identified entities) and '.label_' (the label)

ex4 = nlp("By 2020 the telecom company Orange will relocate from Turkey to Orange County in U.S. close to Apple. It will cost them about 2 million dollars.")

for word in ex4.ents:
    print(word.text, word.label, word.label_)
# what is "GPE"? -> aah, it's "Countries, cities, states" (i.e. Geopolitical entity)
print(spacy.explain('GPE'))

# Jupyter would use displacy.render(ex4, style="ent", jupyter=True), because it's already being served
# displacy.serve(ex4, style="ent")

ex5 = nlp(u"Linus Benedict Torvalds is a Finnish-American software engineer who is the creator and, historically, the principal developer of the Linux kernel, which is the kernel for Linux operating systems (distributions) and other operating systems such as Android and Chrome OS. He also created the distributed version control system Git and the scuba dive logging and planning software Subsurface.")
for word in ex5.ents:
    print(word.text, word.label, word.label_)
# displacy.serve(ex5, style="ent")

# Dependency says something about how words are related to each other (use '.dep_')
# a tricky text, but the cat (who was chased by the dog) killed the rat (the rat which ate the malt)
ex6 = nlp("The rat the cat the dog chased killed ate the malt")
for word in ex6:
    print(word.text, word.pos_, word.dep_)

options = {'compact': True, 'bg': 'cornflowerblue',
           'color': '#fff', 'font': 'Sans Serif'}
# displacy.serve(ex6, style="dep", options=options)
# can be saved as a SVG file as well
svg = displacy.render(ex6, style="dep")
with open('example.svg', 'w', encoding='utf-8') as f:
    f.write(svg)

# Semantic similarity - object1.similarity(object2) - is very useful for recommendation systems (or as data pre-processing to remove duplicates)
ex7 = nlp("wolf")
ex8 = nlp("dog")
ex9 = nlp("cat")
ex10 = nlp("smart")
ex11 = nlp("clever")
ex12 = nlp("wolf dog cat bird fish")
# similarity returns a numerical value describing how similar the words are (range 0-1)
print(ex7.similarity(ex8))
print(ex9.similarity(ex8))
print(ex10.similarity(ex11))

for token1 in ex12:
    for token2 in ex12:
        print((token1.text, token2.text),
              "Similarity =>", token1.similarity(token2))

# or to work with similarity in a dataframe
mylist = [(token1.text, token2.text, token1.similarity(token2))
          for token2 in ex12 for token1 in ex12]
df = pd.DataFrame(mylist)
print(df.head)
print(df.corr())
# correlation doesn't tell us anything; we're missing the column names
df.columns = ["Token1", "Token2", "Similarity"]
print(df.head)

# and of course we can visualise it as well
df_viz = df.replace({'wolf': 0, 'dog': 1, 'cat': 2, 'bird': 3, 'fish': 4})
plt.figure(figsize=(20, 10))
sns.heatmap(df_viz.corr(), annot=True)
# plt.show()


# Stopwords - words that are filtered out before preprocessing; good for getting rid of noise and distractions (remove the most common words)
# from spacy.lang.en.stop_words import STOP_WORDS - there are about 300 for English
print(STOP_WORDS)
# is "the" a stopword? -> True
print(nlp.vocab['the'].is_stop)

# filter out the non-stop words
ex13 = nlp(
    u"This is a sentence about how to use stopwords in natural language processing")

for word in ex13:
    if word.is_stop == True:
        print(word)

# and filtering out the stop words:
for word in ex13:
    if word.is_stop == False:
        print(word)

# as a list
mylist = [word for word in ex13 if word.is_stop == False]
print(mylist)

# Adding/removing your own stopwords -- the stopwords of course reset to default at next model load
print(nlp.vocab['lol'].is_stop)
nlp.vocab['lol'].is_stop = True
print(nlp.vocab['lol'].is_stop)
nlp.vocab['lol'].is_stop = False
print(nlp.vocab['lol'].is_stop)


# Noun Chunks: Noun + word describing the noun (noun phrases, adnominal, root.text)
ex14 = nlp(u"the man reading the news is very tall")
for token in ex14.noun_chunks:
    print(token.text)
for token in ex14.noun_chunks:
    print(token.root.text)
for token in ex14.noun_chunks:
    print(token.root.text, "connecting:", token.root.head.text)

# Sentence segmentation or boundary detection - figuring out where a sentence starts/ends normally:
# a) if it's a period, it ends a sentence
# b) if the preceeding token is in the hand-compiled list of abbreviations, then it doesn't end a sentence
# c) if the next token is capitalised, then it ends a sentence
# Defaults to dependency parser. For custom/manual rules, set boundaries BEFORE parsing the doc.


# Custom boundary function
def my_custom_sentence_boundary_detector(text):
    for token in text[:-1]:
        if token.text == '---':
            text[token.i+1].is_sent_start = True
    return text


# Add the rule before you start processing
nlp.add_pipe(my_custom_sentence_boundary_detector, before='parser')

print(nlp.pipeline)

ex15 = nlp(u"This is my first sentence---the last comment was so cool---what if---? this is the last sentence")

for sentence in ex15.sents:
    print(sentence)


# removing the rule from the pipeline again will make it fail
nlp.remove_pipe('my_custom_sentence_boundary_detector')
ex15a = nlp(
    u"This is my first sentence---the last comment was so cool---what if---? this is the last sentence")
for sentence in ex15a.sents:
    print(sentence)

print(nlp.pipeline)


# Intent classification -- Useful for chatbots etc.
# NLU = unstructured inputs and convert to structured form that a machine can understand and act upon (a subset of NLP)
# ... cannot get rasa_nlu working on this setup.


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
