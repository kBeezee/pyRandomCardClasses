import random
import pyWar
import collections

SUITS = ["spades", "diamonds", "clubs", "hearts"] #8
RANKS = ["ace", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king"] #5

class Deck():
    def __init__(self):
        self.Cards = []

    def addcard(self, myCard):
        self.Cards.append(myCard)

    def makenew52carddesk(self):
        for s in SUITS:
            for r in RANKS:
                pass
                self.addcard(Card(s, r))

class Hand():
    def __init__(self):
        self.Cards = []

    def addcard(self, myCard):
        self.Cards.append(myCard)

    def drawcardontop(self):
        return self.Cards[0]

    def drawwarcard(self):
        oWarCard = 4
        if oWarCard >= len(self.Cards):
            oWarCard = len(self.Cards) - 1
        return self.Cards[oWarCard]

    def WAR_WinRound(self, OtherHand, intWinnings=0):
        if len(OtherHand.Cards) < intWinnings:
            intWinnings = len(OtherHand.Cards)

        #for j in range(0, intWinnings+1):
        self.Cards.append(OtherHand.Cards[0])
        self.Cards.append(self.Cards[0])
        self.Cards.pop(0)
        OtherHand.Cards.pop(0)
        intWinnings -= 1

        while len(OtherHand.Cards) > 0 and intWinnings >= 0:
            BattleString = "    %s .--. %s   %2s - %2s" % (OtherHand.drawcardontop().p0, self.drawcardontop().p0,
                                                           len(OtherHand.Cards), len(self.Cards))
            if intWinnings > 0:
                print BattleString
            self.Cards.append(OtherHand.Cards[0])
            self.Cards.append(self.Cards[0])
            self.Cards.pop(0)
            OtherHand.Cards.pop(0)
            intWinnings -= 1

        return OtherHand

    def POKER_GetStrongestHand(self):
        self.StrongestHand = "None"
        self.intStrongestHand = 0
        #prepase hand for anallysisss
        RankList = []
        SuitList = []
        for c in self.Cards:
            RankList.append(c.intRank)
            SuitList.append(c.Suit)
        RankList = sorted(RankList)

        Pairs = [x for x, y in collections.Counter(RankList).items() if y > 1]
        if len([x for x, y in collections.Counter(RankList).items() if y == 4]) > 0:
            self.StrongestHand = "Four of a Kind"
            self.intStrongestHand = 7
        elif len([x for x, y in collections.Counter(RankList).items() if y == 3]) > 0:
            self.StrongestHand = "Three of a Kind"
            self.intStrongestHand = 3
            if len([x for x, y in collections.Counter(RankList).items() if y == 2]) > 0:
                self.StrongestHand = "Full House"
                self.intStrongestHand = 6
        elif len(Pairs) == 1:
            self.StrongestHand = "Pair"
            self.intStrongestHand = 1
        elif len(Pairs) == 2:
            self.StrongestHand = "Two Pair"
            self.intStrongestHand = 2
        if len(RankList) > 0:
            if RankList[0] == RankList[1] - 1 == RankList[2] -2 == RankList[3] -3 == RankList[4] - 4:
                self.StrongestHand = "Straight"
                self.intStrongestHand = 4
        if len(SuitList) > 0:
            if self.StrongestHand == "Straight" and SuitList[0] == SuitList[1] == SuitList[2] == SuitList[3] == SuitList[4]:
                self.StrongestHand = "Straight Flush"
                self.intStrongestHand = 8
                if 14 in RankList:
                    self.StrongestHand = "Royal Straight Flush"
                    self.intStrongestHand = 9
            elif SuitList[0] == SuitList[1] == SuitList[2] == SuitList[3] == SuitList[4]:
                self.StrongestHand = "Flush"
                self.intStrongestHand = 5
        return self.StrongestHand

class Card():
    def __init__(self, fuSuitName = False, fuRankName = False, fuSuitIndex = False, fuRankIndex = False):
        self.Suit = fuSuitName
        self.Rank = fuRankName

        self.Color = color.BLACK
        if self.Suit == "diamonds" or self.Suit == "hearts":
            self.Color = color.RED

        self.intRank = ranktoint(self.Rank)
        self.p0 = "%s%s of %s%s" % (self.Color, self.Rank, self.Suit, color.END)

    def drawrandomcard(self):
        return RANKS[random.randrange(0, len(RANKS)-1)] + " of " + SUITS[random.randrange(0,len(SUITS)-1)] + "."

class color:
    BLACK = '\033[1m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

    '''
      color = {
    'white':    "\033[1,37m",
    'yellow':   "\033[1,33m",
    'green':    "\033[1,32m",
    'blue':     "\033[1,34m",
    'cyan':     "\033[1,36m",
    'red':      "\033[1,31m",
    'magenta':  "\033[1,35m",
    'black':    "\033[1,30m",
    'darkwhite':  "\033[0,37m",
    'darkyellow': "\033[0,33m",
    'darkgreen':  "\033[0,32m",
    'darkblue':   "\033[0,34m",
    'darkcyan':   "\033[0,36m",
    'darkred':    "\033[0,31m",
    'darkmagenta':"\033[0,35m",
    'darkblack':  "\033[0,30m",
    'off':        "\033[0,0m"
    }'''

def ranktoint(rank):
    if rank.find("ace") >= 0: #", == "ace":
        return 14
    elif rank.find("king") >= 0: #rank == "king":
        return 13
    elif rank.find("queen") >= 0: #rank == "queen":
        return 12
    elif rank.find("jack") >= 0: #rank == "jack":
        return 11
    elif rank.find("ten") >= 0: #rank == "ten":
        return 10
    elif rank.find("nine") >= 0: #rank == "nine":
        return 9
    elif rank.find("eight") >= 0: #rank == "eight":
        return 8
    elif rank.find("seven") >= 0: #rank == "seven":
        return 7
    elif rank.find("six") >= 0: #rank == "six":
        return 6
    elif rank.find("five") >= 0: #rank == "five":
        return 5
    elif rank.find("four") >= 0: #rank == "four":
        return 4
    elif rank.find("three") >= 0: #rank == "three":
        return 3
    elif rank.find("two") >= 0: #rank == "two":
        return 2

