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

#class BlackjackGame(object):

#function to keep score
def keepScore (card, userTotal):
    cardTotal = cardDrawn.cardValue
    userTotal += cardTotal
    return userTotal


cards = [jack, queen, two, three, four, five, six, seven, eight, nine, ten, ace]
cardDeck = cards + cards + cards + cards
shuffle(cardDeck)
userTotal = 0
x = 0
#gets the first two cards laid down for the player
while (x < 2):
    cardDrawn = cardDeck.pop()
    print (cardDrawn.name)
    userTotal = keepScore(cardDrawn, userTotal)
    x = x + 1
dealerTotal = 0

cardDrawn = cardDeck.pop()
print ('One of the dealers cards is a' , cardDrawn.name)
dealerTotal = keepScore(cardDrawn, dealerTotal)
cardDrawn = cardDeck.pop()
hiddenCard = cardDrawn.name
dealerTotal = keepScore(cardDrawn, dealerTotal)

print('Your total is' , userTotal)
if userTotal == 21:
    print('Blackjack')
print("Do you want to hit or stay?(H/S)")
play = input().upper()
#player playing
while play == 'H':
    cardDrawn = cardDeck.pop()
    print("You drew a ", cardDrawn.name)
    userTotal = keepScore(cardDrawn, userTotal)
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
        print('Your total is', userTotal)
        print('Now it is the dealers turn')
if play == "S":
    print('Your total is', userTotal)
    print('Now it is the dealers turn')
#dealer playing
print('The dealers hidden card is a', hiddenCard)
if dealerTotal < 17:
    dealerPlay = "G"
    while dealerPlay == "G":
        cardDrawn = cardDeck.pop()
        print("Dealer played a", cardDrawn.name)
        dealerTotal = keepScore(cardDrawn, dealerTotal)
        if dealerTotal > 21:
            print("Dealer Bust")
            dealerPlay = "X"
        elif dealerTotal > 17:
            print("Dealer total is", dealerTotal)
            dealerPlay = "X"
        elif dealerTotal ==21:
            print("Dealer blackjack")
            dealerPlay = "X"
elif dealerTotal > 17:

    print('The dealers total is', dealerTotal)
elif dealerTotal == 21:
    print('Dealer BlackJack')
#determine who wins