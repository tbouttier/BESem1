import fonctions

fic = 'static/cards/cards.csv'

donne = fonctions.distribCards()

mainJ1= donne[0]
mainJ2= donne[1]
cacheJ1 = donne[2]
cacheJ2 = donne[3]

#for card in mainJ1:
#    print(fonctions.getCardImg(fic,str(card)))

print("\n")

#for card in mainJ2:
#    print(fonctions.getCardImg(fic,str(card)))

st_pl=fonctions.startingPlayer()

#print(st_pl)

#atout = fonctions.getCardColor(fic,str(donne[st_pl][-1]))

#fonctions.saveGame('gameData',None,atout,mainJ1,mainJ2,0,1)

#print(fonctions.loadGame('gameData'))

cards = []

"""for line in donne:
    for card in line:
        cards.append(fonctions.getCardImg(fic,str(card)))"""

jeu = ["carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png"]


print(mainJ1)
print(cacheJ1)
print(jeu)

fonctions.cardPlayed(0,mainJ1,cacheJ1,jeu,'2')

print(mainJ1)
print(cacheJ1)
print(jeu)