import fonctions

fic = 'static/cards/cards.csv'

donne = fonctions.distribCards()

mainJ1= donne[0]
mainJ2= donne[1]
cacheJ1 = donne[2]
cacheJ2 = donne[3]

for card in mainJ1:
    print(fonctions.getCardImg(fic,str(card)))

print("\n")

for card in mainJ2:
    print(fonctions.getCardImg(fic,str(card)))

st_pl=fonctions.startingPlayer()

print(st_pl)

print(fonctions.getCardColor(fic,str(donne[st_pl][-1])))

fonctions.saveGame('gameData',None,atout,main_P1,main_P2,0,1)

print(fonctions.loadGame('gameData'))