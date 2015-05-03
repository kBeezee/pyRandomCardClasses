#!/usr/bin/python

import pylowClasses as pl
import random
import collections
import itertools
import datetime

NewDeck = pl.Deck()
NewDeck.makenew52carddesk()
random.shuffle(NewDeck.Cards)

hand0 = pl.Hand()
decks = 0
pairs = 0
triple = 0
quad = 0
pairresults = []
tripleresults = []
quadresults = []

start = datetime.datetime.now()
while decks < 1234789:
    random.shuffle(NewDeck.Cards)
    pairs = 0
    triple = 0
    quad = 0
    for i in range(len(NewDeck.Cards)-1):
        if i < 49:
            if NewDeck.Cards[i].intRank == NewDeck.Cards[i+1].intRank == NewDeck.Cards[i+2].intRank == \
                    NewDeck.Cards[i+3].intRank:
                quad += 1
                continue
        if i < 50:
            if NewDeck.Cards[i].intRank == NewDeck.Cards[i+1].intRank == NewDeck.Cards[i+2].intRank:
                triple += 1
                continue
        if NewDeck.Cards[i].intRank == NewDeck.Cards[i+1].intRank:
            pairs += 1
    pairresults.append(pairs)
    tripleresults.append(triple)
    quadresults.append(quad)
    decks += 1

SingleResultsPair = [x for x, y in collections.Counter(pairresults).items() if y >= 1]
SingleResultsTriple = [x for x, y in collections.Counter(tripleresults).items() if y >= 1]
SingleResultsQuad = [x for x, y in collections.Counter(quadresults).items() if y >= 1]

print "---" + str(decks) + " Decks of Cards:"
for s, t, q in itertools.izip_longest(SingleResultsPair, SingleResultsTriple, SingleResultsQuad): #, fillvalue=s):
    if t == None:
        t = s
    if q == None:
        q = s

    print "%2s Pairs: %6s - %10f%%  | %2s Triples: %6s - %10f%%  |  %2s Quads: %6s - %10f%%" % \
          (str(s), str(pairresults.count(s)), float(pairresults.count(s))/decks * 100,
           str(t), str(tripleresults.count(t)), float(tripleresults.count(t))/decks * 100,
           str(q), str(quadresults.count(q)), float(quadresults.count(q))/decks * 100)
    #print str(c) + ": " + str(pairresults.count(c))+" - {0:.4f}%".format(float(pairresults.count(c))/decks * 100)

print datetime.datetime.now() - start
