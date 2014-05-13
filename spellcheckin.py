# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# SpellCheckin
# ==========
# 
# Project to spellcheck my writing. Lately I have gotten back into writing. I guess I always have but I've notived it more. I want to develop a new blog for my writing. I have started using Nikola for blogging. It is powered by Python.
# I have been writing text in a nano. I'd like to develop a spell checker to fix the mistakes I write. 
# IPython Notebook doesn't have a spell checker built in.
# Open up this notebook and edit this Markdown for errors.

# <codecell>

import re, collections

def words(text): 
    return re.findall('[a-z]+', text.lower()) 

def train(features):
    model = collections.defaultdict(lambda: 1)
    for f in features:
        model[f] += 1
    return model

NWORDS = train(words(file('testz').read()))

alphabet = 'abcdefghijklmnopqrstuvwxyz'

def edits1(word):
   splits     = [(word[:i], word[i:]) for i in range(len(word) + 1)]
   deletes    = [a + b[1:] for a, b in splits if b]
   transposes = [a + b[1] + b[0] + b[2:] for a, b in splits if len(b)>1]
   replaces   = [a + c + b[1:] for a, b in splits for c in alphabet if b]
   inserts    = [a + c + b     for a, b in splits for c in alphabet]
   return set(deletes + transposes + replaces + inserts)

def known_edits2(word):
    return set(e2 for e1 in edits1(word) for e2 in edits1(e1) if e2 in NWORDS)

def known(words): return set(w for w in words if w in NWORDS)

def correct(word):
    candidates = known([word]) or known(edits1(word)) or known_edits2(word) or [word]
    return max(candidates, key=NWORDS.get)

# <codecell>

known_edits2('chek')

# <codecell>

openpost = open('spellcheckin.ipynb', 'r')

# <codecell>

postdet = openpost.read()

# <codecell>

postdet['metadata']

# <codecell>

postdet.count

# <codecell>

import json

# <codecell>

json.dumps(postdet)

# <codecell>

words('heLLLlo!')

# <codecell>

correct('test')

# <codecell>

edits1('helo')

# <codecell>


# <codecell>

print 'hello world!'

# <rawcell>


# <codecell>


# <codecell>


# <codecell>


