#!/usr/bin/python

import pylowClasses as pl
import random
import collections
import itertools
import datetime
import sys

'''
This takes a deck of cards, shuffles it, and then goes through the deck one card at a time, looking for two cards
whose ranks match. So, **King King**, right next to each other would be 1 pair. **Four Four Four**, would be a triple;
and **Three Three Three Three** would be a quad. a triple does not count as two pairs AND a triple. each pattern only
counts as its largest pattern, then all cards involved are skipped, which effects the count of no pairs (ie. you dont
find a quad, then check the last card of the quad vs the next card in the deck) then it outputs the number of decks
that had 0 pairs, 1 pair, 2 pairs etc.
'''

def UncoverDeck(fooLIMITER):
    NewDeck = pl.Deck()
    NewDeck.makenew52carddesk()

    '''
    #two decks
    Deck2 = pl.Deck()
    Deck2.makenew52carddesk()
    for c in Deck2.Cards:
        NewDeck.Cards.append(c)
    random.shuffle(NewDeck.Cards)
    '''

    hand0 = pl.Hand()
    decks = 0
    pairs = 0
    triple = 0
    quad = 0
    pairresults = []
    tripleresults = []
    quadresults = []

    start = datetime.datetime.now()
    b = start + datetime.timedelta(0, fooLIMITER)
    while datetime.datetime.now() < b: #timed run
    #while pairs < 5: #wait for a specific combo before stopping
    #while decks < fooLIMITER: #specfic number of decks
        random.shuffle(NewDeck.Cards)
        pairs = 0
        triple = 0
        quad = 0
        for i in range(len(NewDeck.Cards)-1):
            if i < 49:
                if NewDeck.Cards[i].intRank == NewDeck.Cards[i+1].intRank == NewDeck.Cards[i+2].intRank == \
                        NewDeck.Cards[i+3].intRank:
                    quad += 1
                    i += 3
                    continue
            if i < 50:
                if NewDeck.Cards[i].intRank == NewDeck.Cards[i+1].intRank == NewDeck.Cards[i+2].intRank:
                    triple += 1
                    i += 2
                    continue
            if NewDeck.Cards[i].intRank == NewDeck.Cards[i+1].intRank:
                i += 1
                pairs += 1
        pairresults.append(pairs)
        tripleresults.append(triple)
        quadresults.append(quad)
        decks += 1

    SingleResultsPair = [x for x, y in collections.Counter(pairresults).items() if y >= 1]
    SingleResultsTriple = [x for x, y in collections.Counter(tripleresults).items() if y >= 1]
    SingleResultsQuad = [x for x, y in collections.Counter(quadresults).items() if y >= 1]

    n = " Count"
    p = "Percent"
    print "%sPatterns  %6s -  %7s      | Patterns    %6s - %8s     |  Patterns  %6s - %8s    %s" % \
          (pl.color.UNDERLINE, n,p,n,p,n,p, pl.color.END)
    UL = ULe = ""
    for s, t, q in itertools.izip_longest(SingleResultsPair, SingleResultsTriple, SingleResultsQuad): #, fillvalue=s):
        if t == None:
            t = s
        if q == None:
            q = s
        if s == max(SingleResultsPair):
            UL = pl.color.UNDERLINE
            ULe = pl.color.END

        print "%s|%2s Pairs: %6s - %10f%%  | %2s Triples: %6s - %10f%%  |  %2s Quads: %6s - %10f%%|%s" % \
              (UL, str(s), str(pairresults.count(s)), float(pairresults.count(s))/decks * 100,
               str(t), str(tripleresults.count(t)), float(tripleresults.count(t))/decks * 100,
               str(q), str(quadresults.count(q)), float(quadresults.count(q))/decks * 100, ULe)

    print "%s%s Decks of Cards in %s%s" % \
                                (pl.color.YELLOW, (decks), str(datetime.datetime.now() - start), pl.color.END)

fooLIMITER = 35 #seconds

UncoverDeck(fooLIMITER)
