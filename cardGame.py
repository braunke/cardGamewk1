from random import shuffle
class Card(object):
    def __init__(self, value, name):

        self.cardValue = value
        self.name = name

jack = Card( 10, 'Jack')
queen = Card(10, 'Queen')
two = Card(2, 'Two')
three = Card(3, 'Three')
four = Card(4, 'Four')
five = Card(5, 'Five')
six = Card(6, 'Six')
seven = Card(7, 'Seven')
eight = Card(8, 'Eight')
nine = Card(9, 'Nine')
ten = Card(10, "Ten")
ace = Card(1, "Ace")

class BlackjackGame(object):

    #creates deck of cards
    def __init__(self):
        cards = [jack, queen, two, three, four, five, six, seven, eight, nine, ten, ace]
        self.cardDeck = cards + cards + cards + cards
        self.userCards = []
        self.dealerCards = []
        self.gameOver = False

    def deal(self):
       shuffle(self.cardDeck)
       self.userCards.extend([self.cardDeck.pop(), self.cardDeck.pop()])
       self.dealerCards.extend([self.cardDeck.pop(), self.cardDeck.pop()])

    # function to calculate score from a hand of cards
    def getScore (self, cards):
        score = 0
        for card in cards:
            score += card.cardValue
        return score

    def getUserScore (self):
        return self.getScore(self.userCards)

    def getDealerScore (self):
        return self.getScore(self.dealerCards)

    def getCards (self, cards, showHidden):
        cardList = ""
        for idx, card in enumerate(cards):
            if (showHidden == False and idx == 1):
                cardList += "Hidden"
            else:
                cardList += card.name
        return cardList

    def getUserCards (self):
        return self.getCards(self.userCards, True)

    def getDealerCards (self):
        return self.getCards(self.dealerCards, self.gameOver)
    def hit(self):
        card = self.cardDeck.pop()
        self.userCards.append(card)
        return card.name
    def stay(self):
        self.gameOver = True
        dealerCards = self.getDealerCards()
        print("So far the dealer has" , dealerCards)
        dealerTotal = self.getDealerScore()
        if dealerTotal < 17:
            dealerPlay = "G"
            while dealerPlay == "G":
                cardDrawn = self.cardDeck.pop()
                print("Dealer played a", cardDrawn.name)
                self.dealerCards.append(cardDrawn)
                dealerTotal = self.getDealerScore()
                if dealerTotal > 21:
                    print("Dealer Bust")
                    print('You win')
                    self.recordWinningScores()
                    dealerPlay = "X"
                elif dealerTotal > 17:
                    print("Dealer total is", dealerTotal)
                    dealerPlay = "X"
                    self.winner()

        elif dealerTotal > 17:
            print('The dealers total is', dealerTotal)
            self.winner()
        elif dealerTotal == 21:
            print('Dealer BlackJack')
            self.winner()
    def winner(self):
        dealerTotal = self.getDealerScore()
        userTotal = self.getUserScore()
        if dealerTotal == 21:
            print(" Blackjack")
            if userTotal == 21:
                print("Both have blackjacks, it is a tie")
                self.recordTies()
            else:
                print('Dealer Wins')
                self.recordLosingScores()
        elif dealerTotal > userTotal:
            print('You lose')
            self.recordLosingScores()
        elif dealerTotal < userTotal:
            print('You win')
            self.recordWinningScores()
    def recordWinningScores(self):
        f = open("scores.txt", "a")
        f.write("Win\n")
        f.close()
    def recordLosingScores(self):
        f = open("scores.txt", "a")
        f.write("Lose\n")
        f.close()
    def recordTies(self):
        f = open("scores.txt", "a")
        f.write("Tie\n")
        f.close()
game = BlackjackGame()
game.deal()
print ('The dealer has ' , game.getDealerCards())

print('Your cards:', game.getUserCards())
print('Your total is' , game.getUserScore())

print("Do you want to hit or stay?(H/S)")
play = input().upper()
#player playing
while play == 'H':
    cardDrawn = game.hit()
    print("You drew a ", cardDrawn)
    userTotal = game.getUserScore()
    print("Total is", userTotal)
    if userTotal < 21:
        play = input('Do you want to hit or stay?(H/S)')
    elif userTotal == 21:
        print('Blackjack')
        play = "x"
    elif userTotal > 21:
        print('bust! Game Over')
        play = "x"

if play == "S":
    print('Your total is', game.getUserScore())
    print('Now it is the dealers turn')
    game.stay()

checkScores = input('Do you want to check your playing history?(Y/N)')
if checkScores == "Y":
    f = open("scores.txt", "r")
    print(f.read())