import csv, random, ast

def checkBelote(main):
    """
    Vérifie si le joueur détient une belote dans sa main
    """

def distribCards():
    """
    Crée une liste des valeurs des cartes de 1 à 32
    Mélange et distribue les cartes aux joueurs
    :return tuple: 2 listes main_J1, main_J2
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

def getCardColor(fic: str,valeur: str):
    """
    Renvoi la couleur d'une carte en fonction de sa valeur
    :param valeur str : Utilise la valeur de la carte pour rechercher la couleur (doit être convertie en str)
    :return str couleur: Renvoit la couleur de la carte entrée
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
    :return int : Renvoit le numéro du joueur d'atout 
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

