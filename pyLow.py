import pylowClasses as pl
import random

def highlow():
    HistoricalEducatedGuess()

def HistoricalEducatedGuess():
    def WinLoss(Guess, cVR, cHR):
        loss = win = 0
        if Guess.find("Higher.") > 0:
            if cVR > cHR:
                loss = 1
            else:
                win = 1
        else:
            if cVR >= cHR:
                win = 1
            else:
                loss = 1
        return [win, loss]
    def TakeAGuess(vR):
        TheBigGuess = ""
        #count up to 14: =8, random/ >8, high/ <8 low
        if 14 - vRank > 8:
            TheBigGuess = str(i) + "- Higher."
        elif 14 - vRank < 8:
            TheBigGuess = str(i) + "- Lower."
        else:
            if random.randrange(0, 1) == 0:
                TheBigGuess = str(i) + "- Higher."
            else:
                TheBigGuess = str(i) + "- Lower."
        return TheBigGuess

    def MakeADecision(vR, remainingdeck):
        TheBigGuess = ""
        if len(remainingdeck.Cards) >= 51:
            return TakeAGuess(vR)

        bigger = smaller = same = 0

        for cPotential in remainingdeck.Cards:
            if pl.ranktoint(cPotential.Rank) > vR:
                bigger += 1
            elif pl.ranktoint(cPotential.Rank) < vR:
                smaller += 1
            else:
                same += 1

        #print "b%s - s%s" % (bigger, smaller)

        if bigger > smaller:
            TheBigGuess = str(i) + "- Higher."
        else:
            TheBigGuess = str(i) + "- Lower."
        return TheBigGuess

    NewDeck = pl.Deck()
    NewDeck.makenew52carddesk()
    discard = pl.Hand()

    loss = win = 0
    r = random.randrange(0, len(NewDeck.Cards))
    VisibleCard = NewDeck.Cards.pop(r)
    print VisibleCard.p0
    i = 2
    while len(NewDeck.Cards) > 0:
        vRank = pl.ranktoint(VisibleCard.Rank)
        r = random.randrange(0, len(NewDeck.Cards))
        HiddenCard = NewDeck.Cards.pop(r)
        hRank = pl.ranktoint(HiddenCard.Rank)

        TheBigGuess = MakeADecision(vRank, NewDeck)

        print "   %1s %s" % (TheBigGuess[:2], TheBigGuess[2:])

        gResults = WinLoss(TheBigGuess, vRank, hRank)
        i += 1
        win += gResults[0]
        loss += gResults[1]
        discard.addcard(VisibleCard)
        VisibleCard = HiddenCard
        print VisibleCard.p0
        if len(NewDeck.Cards) > 0:
            r = random.randrange(0, len(NewDeck.Cards))

        print "Win: %2s Loss: %2s" % (win, loss)




def NonHistoricalEducatedGuess():
    def WinLoss(Guess, cVR, cHR):
        loss = win = 0
        if Guess.find("Higher.") > 0:
            if cVR > cHR:
                loss = 1
            else:
                win = 1
        else:
            if cVR > cHR:
                win = 1
            else:
                loss = 1
        return [win, loss]

    NewDeck = pl.Deck()
    NewDeck.makenew52carddesk()
    loss = win = 0
    r = random.randrange(0, len(NewDeck.Cards))
    VisibleCard = NewDeck.Cards.pop(r)
    print VisibleCard.p0
    i = 2
    while len(NewDeck.Cards) > 0:
        vRank = pl.ranktoint(VisibleCard.Rank)
        r = random.randrange(0, len(NewDeck.Cards))
        HiddenCard = NewDeck.Cards.pop(r)
        hRank = pl.ranktoint(HiddenCard.Rank)

        #count up to 14: =8, random/ >8, high/ <8 low
        if 14 - vRank > 8:
            TheBigGuess = str(i) + "- Higher."
        elif 14 - vRank < 8:
            TheBigGuess = str(i) + "- Lower."
        else:
            if random.randrange(0, 1) == 0:
                TheBigGuess = str(i) + "- Higher."
            else:
                TheBigGuess = str(i) + "- Lower."

        print "   %1s %s" % (TheBigGuess[:2], TheBigGuess[2:])
        gResults = WinLoss(TheBigGuess, vRank, hRank)
        i += 1
        win += gResults[0]
        loss += gResults[1]
        VisibleCard = HiddenCard
        print VisibleCard.p0
        if len(NewDeck.Cards) > 0:
            r = random.randrange(0, len(NewDeck.Cards))

        print "Win: %2s Loss: %2s" % (win, loss)

def UserInput():
    NewDeck = pl.Deck()
    NewDeck.makenew52carddesk()
    loss = win = 0

    r = random.randrange(0, len(NewDeck.Cards))
    VisibleCard = NewDeck.Cards.pop(r)
    i = 1
    low = "'"
    high = "["

    while len(NewDeck.Cards) > 0:
        print VisibleCard.p0
        vRank = pl.ranktoint(VisibleCard.Rank)
        HiddenCard = NewDeck.Cards.pop(r)
        hRank = pl.ranktoint(HiddenCard.Rank)

        inpt = ""
        while inpt != low and inpt != high:
            inpt = raw_input(str(i) + "-> ")

        if inpt == high:
            if vRank > hRank:
                loss += 1
            else:
                win += 1
        else:
            if vRank >= hRank:
                win += 1
            else:
                loss += 1
        i += 1
        VisibleCard = HiddenCard
        r = random.randrange(0, len(NewDeck.Cards)-1)
        print "Win: %2s Loss: %2s" % (win, loss)

highlow()

