import pylowClasses as pl
import random


def war():
    NewDeck = pl.Deck()
    NewDeck.makenew52carddesk()

    hand0 = pl.Hand()
    hand1 = pl.Hand()

    drawcount = 0
    warcount = 0

    # Deal Cards
    while len(NewDeck.Cards) > 0:
        r = random.randrange(0, len(NewDeck.Cards))
        hand0.addcard(NewDeck.Cards[r])
        NewDeck.Cards.pop(r)

        r = random.randrange(0, len(NewDeck.Cards))
        hand1.addcard(NewDeck.Cards[r])
        NewDeck.Cards.pop(r)

    #war till winner
    while len(hand0.Cards) < 52 and len(hand1.Cards) < 52:
        drawcount += 1
        if drawcount % 1 == 0:
            BattleString = "%s: %s .vs. %s   %2s - %2s" % (drawcount,
                                        hand0.drawcardontop().p0,
                                        #len(hand0.Cards), len(hand1.Cards),
                                        hand1.drawcardontop().p0, len(hand0.Cards), len(hand1.Cards))
        else:
            BattleString = "%s: %s .vs. %s" % (drawcount,
                                        hand0.drawcardontop().p0,
                                        #len(hand0.Cards), len(hand1.Cards),
                                        hand1.drawcardontop().p0)

        if hand0.drawcardontop().intRank > hand1.drawcardontop().intRank:
            print BattleString
            #print "Player 1 Won."
            hand1 = hand0.WAR_WinRound(hand1)
        elif hand0.drawcardontop().intRank < hand1.drawcardontop().intRank:
            print BattleString
            #print "Player 2 Won"\
            hand0 = hand1.WAR_WinRound(hand0)
        else:  # todo deal with double/triple/quadruple war.
            warcount += 1

            print "  %sWar!!%s %s %s %s .vs. %s %s %s" % (pl.color.PURPLE, pl.color.END,
                                                            pl.color.BOLD, hand0.drawcardontop().p0, pl.color.END,
                                                        #len(hand0.Cards), len(hand1.Cards),
                                                                pl.color.BOLD, hand1.drawcardontop().p0, pl.color.END)

            h0WarCard = hand0.drawwarcard().p0
            h1WarCard = hand1.drawwarcard().p0

            if hand0.drawwarcard().intRank > hand1.drawwarcard().intRank:
                hand1 = hand0.WAR_WinRound(hand1, 4)
            else: # player 2 has a slight advantage here.
                hand0 = hand1.WAR_WinRound(hand0, 4)

            print "    %s^---%s %s %s %s .vs. %s %s %s" % (pl.color.PURPLE, pl.color.END,
                                                        pl.color.BOLD, h0WarCard, pl.color.END,
                                                        #len(hand0.Cards), len(hand1.Cards),
                                                            pl.color.BOLD, h1WarCard, pl.color.END)
        #" - %-10s %-4s %-5s"
        #print "\t\tPlayer 1 has %2s cards Player 2 has %2s cards" % (len(hand0.Cards), len(hand1.Cards))

    if len(hand0.Cards) == 52:
        print "Player 1 wins the war!"
    elif len(hand1.Cards) == 52:
        print "Player 2 wins the war!"

    print "Draw Count: %2s War Count: %s" % (drawcount, warcount)