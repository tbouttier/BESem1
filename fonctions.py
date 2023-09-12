import csv, random, ast
from enum import IntEnum



def checkBelote(main):
    """
    Vérifie si le joueur détient une belote dans sa main
    """

def cardPlayed(joueur, donne, carte_jouee):
    """Joue la carte choisie par le joueur

    Args:
        joueur (int): numéro du joueur
        donne (_type_): 
        carte_jouee (_type_): _description_
    """
        
    return

def distribCards():
    """
    Crée une liste des valeurs des cartes de 1 à 32
    Mélange et distribue les cartes aux joueurs
    
    
    :return (tuple): 4 listes main_J1, main_J2, cacheJ1, cacheJ2
    """
    cards = []
    for value in range(1, 33):
        cards.append(value)
    
    random.shuffle(cards)
    player1 = []
    vis1 = []
    cache1 = []
    player2 = []
    vis2 = []
    cache2 =[]
    
    for i in range(0,32):
        if i%2==0:
            player2.append(cards[i])
        else:
            player1.append(cards[i])

    for vis_card in range(8,16):
        vis1.append(player1[vis_card])
        vis2.append(player2[vis_card])

    for hid_card in range(0,8):
        cache1.append(player1[hid_card])
        cache2.append(player2[hid_card])

    return vis1,vis2,cache1,cache2

def getCardValue(fic,img_name):
    """
    Renvoi la valeur de la carte en fonction du filename de l'image
    :param str fic: fichier .csv contenant les valeurs des cartes et les noms des images
    :param string img_name: Nom du fichier img de la carte recherchée
    :return str valeur
    """
    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['file'] == img_name:
                valeur: str = card.get('Valeur')

    return valeur

def getCardImg(fic: str, valeur: str):
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

def getCardColor(fic: str,valeur: str):
    """
    Renvoi la couleur d'une carte en fonction de sa valeur
    :param valeur (str) : Utilise la valeur de la carte pour rechercher la couleur (doit être convertie en str)
    :return couleur (str): Renvoit la couleur de la carte entrée
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
    :return int : Renvoit le numéro du joueur commençant la partie
    """
    joueur = random.randint(0,1)
    return joueur

def saveGame(save_fic: str,joueur: int,atout: str,mainJ1 : list,mainJ2: list,scores : int,nb_pli: int):
    """
    Sauvegarde les données de la parties en cours dans un fichier gameData
    """
    save_file = open(save_fic,'w')
    save_data = [joueur,atout,mainJ1,mainJ2,scores,nb_pli]
    save_file.write(str(save_data))
    save_file.close()

#TODO Pour Yann : loadGame()
def loadGame(save_fic):
    load_file = open(save_fic,'r')
    game_data = ast.literal_eval(load_file.read())
    return game_data
