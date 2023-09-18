import csv, random, ast, copy
from enum import IntEnum

def init_game():
    """Initialise une nouvelle partie :
    - crée un dictionnaire pour chaque carte
    - crée les listes de cartes des différentes mains des joueurs
    
    Format des cartes:
        {'valeur':__valeur_de_1_à_32__,'image':"__filename.png__"}
        valeur : int
        image : str
    Returns:
        (mainJ1,mainJ2,cache1,cache2) : Les mains des joueurs et les cartes cachés\n
        tuple(list,list,list,list)
    """
    
    init_game()

    card_file ='static/cards/cards.csv'

    donne = distribCards()
    mainJ1 = []
    mainJ2 = []
    cacheJ1 = []
    cacheJ2 = []

    for card in donne[0]:
        mainJ1.append({'valeur':card, 'image':getCardImg(card_file, str(card))})
    for card in donne[1]:
        mainJ2.append(({'valeur':card, 'image':getCardImg(card_file, str(card))}))
    for card in donne[2]:
        cacheJ1.append({'valeur':card, 'image':getCardImg(card_file, str(card))})
    for card in donne[3]:
        cacheJ2.append({'valeur':card, 'image':getCardImg(card_file, str(card))})

    return mainJ1,mainJ2,cacheJ1,cacheJ2

def checkBelote(main):
    """
    Vérifie si le joueur détient une belote dans sa main
    """

def cardPlayed(tour,mainJoueur : list,cacheJoueur:list,tapis_joueur:list,carte_jouee:int,indice_carte:int):
    """Joue la carte sélectionné par le joueur, la déplace sur le tapis et retourne la carte face cachée

    Args:
        tour (int): _description_
        mainJoueur (list): liste des cartes de la main du joueur
        cacheJoueur (list): liste des cartes face cachées du joueur
        tapis_joueur (list): Liste contenant les carte joué par ce joueur pour ce pli
        carte_jouee (int): valeur de la carte jouée (de 1 à 32)
        indice_carte (int): Indice de position de la carte dans la main
    """
    if type(carte_jouee) != int:
        raise TypeError(f"carte_jouee doit être un int pas {type(carte_jouee)}")

    tapis_joueur[indice_carte-1] = copy.deepcopy(mainJoueur[indice_carte-1])
    mainJoueur[indice_carte-1] = copy.deepcopy(cacheJoueur[indice_carte-1])
    cacheJoueur[indice_carte-1]['image'] = 'carte_0.png'


def distribCards():
    """Distribution des cartes:
    - Crée une liste des valeurs des cartes de 1 à 32
    - Mélange et distribue les cartes dans des listes pour les joueurs
    
    Format des listes:
        [int,int,int,int,int,int,int,int]\n
        (int =< 32)
    
    Returns:
        (main_J1, main_J2, cacheJ1, cacheJ2)\n
        tuple(list,list,list,list)
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
    """Renvoi la valeur de la carte en fonction du filename de l'image

    Args:
        fic (str): fichier .csv contenant les valeurs des cartes et les noms des images
        img_name (str): Nom du fichier img de la carte recherchée

    Returns:
        str: valeur de la carte ('1' à '32')
    """
    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['file'] == img_name:
                valeur = card.get('Valeur')

    return valeur

def getCardImg(fic: str, valeur: str):
    """Renvoit le filename de l'image en fonction de la valeur de la carte
    
    Args:
        fic (str): fichier .csv contenant les valeurs des cartes et les noms des images
        valeur (int): valeur de la carte recherchée
    
    Returns:
        imgName (str) : nom du fichier de l'image correspondant à la carte
    """
    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['Valeur'] == valeur:
                imgName: str = card.get('file')

    return imgName

def getCardColor(fic: str,valeur: str):
    """Renvoi la couleur d'une carte en fonction de sa valeur
    
    Args:
        valeur (str) : Utilise la valeur de la carte pour rechercher la couleur
    
    Returns:
        couleur (str): Renvoit la couleur de la carte entrée
    """
    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['Valeur'] == valeur:
                couleur: str = card.get('Couleur')

    return couleur


def startingPlayer():
    """Determine le joueur commençant la partie
    
    Returns:
        joueur (int) : Renvoit le numéro du joueur commençant la partie (0,1)
    """
    joueur = random.randint(0,1)
    return joueur

def saveGame(save_fic: str,joueur: int,atout: str,mainJ1 : list,mainJ2: list,scores : int,nb_pli: int):
    """Sauvegarde les données de la parties en cours dans un fichier gameData
    """
    save_file = open(save_fic,'w')
    save_data = [joueur,atout,mainJ1,mainJ2,scores,nb_pli]
    save_file.write(str(save_data))
    save_file.close()

def loadGame(save_fic):
    load_file = open(save_fic,'r')
    game_data = ast.literal_eval(load_file.read())
    return game_data

def cards_points(fic, atout, valeur):
    Couleur=getCardColor(fic, valeur)
    print(Couleur)
    if Couleur == atout :
        if valeur == ('1' or '9' or '17' or '25'):
            points =11
        if valeur == ('2' or '10' or '18' or '26'):
            points =4
        if valeur == ('3' or '11' or '19' or '27'):
            points=3
        if valeur == ('4' or '12' or '20' or '28'):
            points =20
        if valeur == ('5' or '13' or '21' or '29'):
            points =10
        if valeur == ('6' or '14' or '22' or '30'):
            points =14
        if valeur == ('7' or '15' or '23' or '31'):
            points = 0
        if valeur == ('8' or '16' or '24' or '32'):
            points =0
    else:
        if valeur == ('1' or '9' or '17' or '25'):
            points =11
        if valeur == ('2' or '10' or '18' or '26'):
            points =4
        if valeur == ('3' or '11' or '19' or '27'):
            points=3
        if valeur == ('4' or '12' or '20' or '28'):
            points =2
        if valeur == ('5' or '13' or '21' or '29'):
            points =10
        if valeur == ('6' or '14' or '22' or '30'):
            points =0
        if valeur == ('7' or '15' or '23' or '31'):
            points = 0
        if valeur == ('8' or '16' or '24' or '32'):
            points =0
    return points

