import csv
import random

def distribCards():
    """
    Crée une liste des valeurs des cartes de 1 à 32
    Mélange et distribue les cartes aux joueurs
    """
    cards = []
    for value in range(1, 33):
        cards.append(value)
    
    random.shuffle(cards)
    player1 = []
    player2 = []
    for i in range(0,32):
        if i%2==0:
            player2.append(cards[i])
        else:
            player1.append(cards[i])
    return player1,player2

def getCardImg(fic: str, valeur: int):
    """
    Renvoi le filename de l'image en fonction de la valeur de la carte
    :param str fic: fichier .csv contenant les valeurs des cartes et les noms des images
    :param int valeur: valeur de la carte recherchée
    :return str imgName
    """
    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['Valeur'] == valeur:
                imgName: str = card.get('file')

    return imgName

def getCardColor(fic: str,valeur: int):
    """
    Renvoi la couleur d'une carte en fonction de sa valeur
    """
    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['Valeur'] == valeur:
                couleur: str = card.get('Couleur')

    return couleur


def startingPlayer():
    """
    Determine le joueur commençant la partie
    """
    joueur = random.randint(0,1)

    return joueur

#TODO Savegame
def saveGame(save_file,joueur,mainJ1,mainJ2,scores,nb_pli):
    open(save_file,'w')