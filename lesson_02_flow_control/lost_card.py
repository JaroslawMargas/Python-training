# There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost
# card given the numbers for the remaining cards N-1
#


num_card = int(input("How many cards?"))

list_card = []
x = 0
while x != num_card:

    card = int(input("Provide card"))
    print(x)
    print(num_card)
    if card in list_card:
        print("you can't add the same card")
    else:
        list_card.append(card)
        x += 1

x = 0
while x != (num_card-1):
    print("which card do you have?")
    card = int(input())
    if card not in list_card:
        print("you can't have this card")
    else:
        list_card.remove(card)
        x += 1

print("card lost:"+str(list_card[0]))

