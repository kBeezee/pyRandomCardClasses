#!/usr/bin/python

import pylowClasses as pl
import random
import collections

NewDeck = pl.Deck()
NewDeck.makenew52carddesk()

hand0 = pl.Hand()
hand1 = pl.Hand()
DealCount = 1


# Deal Cards
for i in range(5):
    r = random.randrange(0, len(NewDeck.Cards))
    hand0.addcard(NewDeck.Cards[r])
    NewDeck.Cards.pop(r)

Results = []

#while hand0.POKER_GetStrongestHand() != "Royal Straight Flush":
while DealCount < 10000:
    NewDeck = pl.Deck()
    NewDeck.makenew52carddesk()

    hand0 = pl.Hand()

    # Deal Cards
    for i in range(5):
        r = random.randrange(0, len(NewDeck.Cards))
        hand0.addcard(NewDeck.Cards[r])
        NewDeck.Cards.pop(r)

    for i in range(len(hand0.Cards)):
        pass
        #print hand0.Cards[i].p0

    h0Result = hand0.POKER_GetStrongestHand()

    print str(DealCount) + " - " + h0Result
    Results.append(h0Result)
    DealCount += 1

print "---" + str(DealCount) + " Deals"
print "Nothing: " + str(Results.count("None")) + " - " + "{0:.1f}%".format(float(Results.count("None"))/DealCount * 100)
print "Pairs: " + str(Results.count("Pair")) + " - " + "{0:.1f}%".format(float(Results.count("Pair"))/DealCount * 100)
print "Two Pair: " + str(Results.count("Two Pair")) + " - " + "{0:.1f}%".format(float(Results.count
                                                                                     ("Two Pair"))/DealCount * 100)
print "Three of a Kind: " + str(Results.count("Three of a Kind"))+ " - " + "{0:.1f}%".format(float(Results.count
                                                                                   ("Three of a Kind"))/DealCount * 100)
print "Straight: " + str(Results.count("Straight")) + " - " + "{0:.6f}%".format(float(Results.count
                                                                                      ("Straight"))/DealCount * 100)
print "Flush: " + str(Results.count("Flush")) + " - " + "{0:.1f}%".format(float(Results.count("Flush"))/DealCount * 100)
print "Full House: " + str(Results.count("Full House")) + " - " + "{0:.6f}%".format(float(Results.count
                                                                                      ("Full House"))/DealCount * 100)
print "Four of a Kind: " + str(Results.count("Four of a Kind")) + " - " + "{0:.6f}%".format(float(Results.count
                                                                                    ("Four of a Kind"))/DealCount * 100)
print "Straight Flush: " + str(Results.count("Straight Flush")) + " - " + "{0:.6f}%".format(float(Results.count
                                                                                  ("Straight Flush"))/DealCount * 100)
print "Royal Straight Flush: " + str(Results.count("Royal Straight Flush")) + " - " + "{0:.6f}%".format(float(
    Results.count ("Royal Straight Flush"))/DealCount * 100)
#"Royal Straight Flush"