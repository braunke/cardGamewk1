from random import shuffle
#creates the cards
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
#class for the game
class BlackjackGame(object):

    #creates deck of cards
    def __init__(self):
        cards = [jack, queen, two, three, four, five, six, seven, eight, nine, ten, ace]
        self.cardDeck = cards + cards + cards + cards
        self.userCards = []
        self.dealerCards = []
        self.gameOver = False
    #shuffles the deck and gives the player and dealer each two cards
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
    #functions to get the user and dealer score
    def getUserScore (self):
        return self.getScore(self.userCards)

    def getDealerScore (self):
        return self.getScore(self.dealerCards)
    #gets the cards the players have
    def getCards (self, cards, showHidden):
        cardList = ""
        for idx, card in enumerate(cards):
            if (showHidden == False and idx == 1):
                cardList += "Hidden "
            else:
                cardList += card.name + " "
        return cardList

    def getUserCards (self):
        return self.getCards(self.userCards, True)

    def getDealerCards (self):
        return self.getCards(self.dealerCards, self.gameOver)
    #what happens when a palyer hits
    def hit(self):
        card = self.cardDeck.pop()
        self.userCards.append(card)
        return card.name
    #what happens when a player stays, goes into the dealer playing
    def stay(self):
        self.gameOver = True
        dealerCards = self.getDealerCards()
        print("So far the dealer has" , dealerCards)
        dealerTotal = self.getDealerScore()
        #determines if the dealer will hit or not
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
    #if it has not been determined this sees who wins
    def winner(self):
        dealerTotal = self.getDealerScore()
        userTotal = self.getUserScore()
        if dealerTotal == 21:
            print("Dealer Blackjack")
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
        elif dealerTotal == userTotal:
            self.recordTies()
    #records the results of the game to a file
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
playOn = True
#allows you to keep playing the game
while playOn == True:
    game = BlackjackGame()
    game.deal()
    print ('The dealer has ', game.getDealerCards())

    print('Your cards:', game.getUserCards())
    print('Your total is' , game.getUserScore())

    print("Do you want to hit or stay?(H/S)")
    play = input().upper()
    while play != "H" and play != "S":
                print("Please enter a valid response")
                play = input().upper()
    #player playing
    while play == 'H':
        cardDrawn = game.hit()
        print("You drew a ", cardDrawn)
        userTotal = game.getUserScore()
        print("Total is", userTotal)
        if userTotal < 21:
            print('Do you want to hit or stay?(H/S)')
            play = input().upper()
            while play != "H" and play !="S":
                print("Please enter a valid response")
                play = input().upper()
        elif userTotal == 21:
            print('Blackjack')
            play = "S"
        elif userTotal > 21:
            print('bust! Game Over')
            play = "x"

    if play == "S":
        print('Your total is', game.getUserScore())
        print('Now it is the dealers turn')
        game.stay()

    print('Do you want to check your playing history?(Y/N)')
    checkScores = input().upper()
    while checkScores != "Y" and checkScores != "N":
                print("Please enter a valid response")
                checkScores = input().upper()
    if checkScores == "Y":
        f = open("scores.txt", "r")
        print(f.read())
    print("Would you like to play again?(Y/N)")
    keepPlaying = input().upper()
    while keepPlaying != "Y" and keepPlaying != "N":
                print("Please enter a valid response")
                keepPlaying = input().upper()
    if keepPlaying == "Y":
      playOn = True

    else:
       playOn = False