import fonctions

fic = 'static/cards/cards.csv'

mainJ1_IMG = []
mainJ2_IMG = []
cacheJ1_IMG = []
cacheJ2_IMG = []

donne = fonctions.init_game()

tapis1 = ["carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png"]
tapis2 = ["carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png"]


donneIMG = (donne[0], donne[2],tapis1,tapis2,donne[3],donne[1])
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

print(fonctions.cards_points(fic,'Carreau', '29'))

#print(fonctions.getCardValue(fic,mainJ1[2]))

