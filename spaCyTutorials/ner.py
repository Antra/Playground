# Training our NER
# - Load the model
# -- e.g. spacy.load('en') -- remember to disable existing pipeline (nlp.disable_pipes)
# -- or spacy.blank('en') -- to load a blank model; remember to add a Entity Recogniser to Pipeline
# - Shuffle and loop over the examples
# -- Update the model (nlp.update) in every iteration
# - Save the trained model to disk (nlp.to_disk)
# - Test
# See:
# - https://www.youtube.com/watch?v=81OK6WHb_Q0&list=PLJ39kWiJXSiz1LK8d_fyxb7FTn4mBYOsD&index=14
# - https://github.com/explosion/spaCy/blob/master/examples/training/train_new_entity_type.py


import plac  # wrapper over argparse
import random
from pathlib import Path
import spacy
from tqdm import tqdm  # loading bar


nlp1 = spacy.load('en')

ex1 = nlp1(u"Who was Kofi Annan?")

# Training dataset must include the start_char/end_char for the model to improve
for token in ex1.ents:
    print(token.text, token.start_char, token.end_char, token.label_)

ex2 = nlp1(u"Who is Steve Jobs?")
for token in ex2.ents:
    print(token.text, token.start_char, token.end_char, token.label_)

ex3 = nlp1(u"Who was Shaka Khan?")
for token in ex3.ents:
    print(token.text, token.start_char, token.end_char, token.label_)


# Training data set
TRAIN_DATA = [
    ('Who is Kofi Annan?', {
        'entities': [(8, 18, 'PERSON')]
    }),
    ('Who is Steve Jobs?', {
        'entities': [(7, 17, 'PERSON')]
    }),
    ('I like London and Berlin?', {
        'entities': [(7, 13, 'LOC'), (18, 24, 'LOC')]
    }),
    ('I have been to Paris!', {
        'entities': [(15, 20, 'LOC')]
    }),
]


# Annotate -- cannot get this working, skip for now.
# @plac.annotations(
#    model=("Model name. Defaults to blank 'en' model.", "option", "m", str),
#    output_dir=("G:\\Projects\\spaCyTutorials\\models", "option", "o", Path),
#    n_iter=("Number of training iterations", "option", "n", int))
# Define the variables
model = 'models'
output_dir = Path("G:\\Projects\\spaCyTutorials\\models")
n_iter = 100

if model is not None:
    nlp = spacy.load(model)  # Load existing spaCy model
    print("Loaded model '%s'" % model)
else:
    nlp = spacy.blank('en')  # Create blank model class
    print("Created blank 'en' model")

# Create the built-in pipeline components and add them to the pipeline
# nlp.create_pipe works for built-ins that are registered with spaCy
if 'ner' not in nlp.pipe_names:
    ner = nlp.create_pipe('ner')
    nlp.add_pipe(ner, last=True)
# otherwise, get it so we can add labels
else:
    ner = nlp.get_pipe('ner')

# then train the recogniser
# - add labels
# - annotate them
# - pipes
# - begin_training()

# add labels
for _, annotations in TRAIN_DATA:
    for ent in annotations.get('entities'):
        ner.add_label(ent[2])

# get names of other pipes to disable them during training
other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']
with nlp.disable_pipes(*other_pipes):  # only train NER!
    optimiser = nlp.begin_training()
    for itn in range(n_iter):
        random.shuffle(TRAIN_DATA)
        losses = {}
        # tqdm() can be omitted if needs be; just displays a nice loading bar
        for text, annotations in tqdm(TRAIN_DATA):
            nlp.update(
                [text],  # batch of texts
                [annotations],  # batch of annotations
                drop=0.5,  # dropout - make it harder to memorise data
                sgd=optimiser,  # callable to update weights
                losses=losses
            )
        print(losses)


# Test the trained model
for text, _ in TRAIN_DATA:
    doc = nlp(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
    print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])


# Saving the model
if output_dir is not None:
    output_dir = Path(output_dir)
    if not output_dir.exists():
        output_dir.mkdir()
    nlp.to_disk(output_dir)
    print("Saved model to", output_dir)

# Test the saved model
print('Loading from', output_dir)
nlp2 = spacy.load(output_dir)
for text, _ in TRAIN_DATA:
    doc = nlp2(text)
    print('Entities', [(ent.text, ent.label_) for ent in doc.ents])
    print('Tokens', [(t.text, t.ent_type_, t.ent_iob) for t in doc])
