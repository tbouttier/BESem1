import csv, random, ast, copy

card_file ='static/cards/cards.csv'


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

    card_file ='static/cards/cards.csv'

    donne = distribCards()
    mainJ1 = []
    mainJ2 = []
    cacheJ1 = []
    cacheJ2 = []

    for card in donne[0]:
        mainJ1.append({'valeur':card, 'image':getCardImg(card_file, str(card)), 'figure':getCardFigure(card_file,str(card))})
    for card in donne[1]:
        mainJ2.append({'valeur':card, 'image':getCardImg(card_file, str(card)), 'figure':getCardFigure(card_file,str(card))})
    for card in donne[2]:
        cacheJ1.append({'valeur':card, 'image':'dos.jpg', 'figure':getCardFigure(card_file,str(card))})
    for card in donne[3]:
        cacheJ2.append({'valeur':card, 'image':'dos.jpg', 'figure':getCardFigure(card_file,str(card))})

    return mainJ1,mainJ2,cacheJ1,cacheJ2


def cardPlayed(mainJoueur : list, cacheJoueur:list, tapis_joueur:list, carte_jouee:int, indice_carte:int):
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

    tapis_joueur[0] = copy.deepcopy(mainJoueur[indice_carte-1])
    mainJoueur[indice_carte-1] = copy.deepcopy(cacheJoueur[indice_carte-1])
    mainJoueur[indice_carte-1]['image'] = getCardImg(card_file,str(mainJoueur[indice_carte-1]['valeur']))
    cacheJoueur[indice_carte-1]['image'] = None
    cacheJoueur[indice_carte-1]['valeur'] = None
    cacheJoueur[indice_carte-1]['figure'] = None


def checkTapis(tapisJ1:dict, tapisJ2:dict, atout:str, score:list, joueur:list, pli:list):
    """érifie que les 2 joueurs aient joué le pli et retourne le gagnant et le score

    Args:
        tapisJ1 (dict): tapis côté joueur 1
        tapisJ2 (dict): tapis côté joueur 2
        atout (str): couleur d'atout de la partie
        score (list): scores des joueurs
        joueur (list): joueur ayant la main
        pli (list): n° pli en cours

    Returns:
        tuple[gagnant,score,joueur]: gagnant du pli (0 ou 1), liste des scores, le joueur qui a la main
    """
    
    cardJ1 = tapisJ1.get('valeur')
    cardJ2 = tapisJ2.get('valeur')
    if (cardJ1 != None and cardJ2 != None):
        pli[0]+=1
        gagnant,points = compareCards(cardJ1,cardJ2,atout)
        if gagnant != None:
            score[gagnant]+=points
            joueur[0] = gagnant

        if pli[0] == 16: #10 de DER
            score[gagnant]+=10
        tapisJ1.clear()
        tapisJ2.clear()
        
        return gagnant,score,joueur
        
        
    

def compareCards(cardJ1:int,cardJ2:int,atout:str):
    """Compare les cartes jouées pour déterminer le gagnant du pli

    Args:
        cardJ1 (int): valeur de la carte du pli du joueur 1
        cardJ2 (int): valeur de la carte du pli du joueur 2
        atout (str): atout de la partie
    Returns:
        tuple[None | int, int] : tuple contenant l'indice du gagnant(0,1) et les point marqués
            gagnant = None si égalité
    """
    point_cardJ1 = cards_points(card_file, atout,cardJ1)
    point_cardJ2 = cards_points(card_file, atout,cardJ2)
    
    if point_cardJ1>point_cardJ2:
        gagnant = 0
        points = point_cardJ1
    elif point_cardJ1<point_cardJ2:
        gagnant = 1
        points = point_cardJ2
    elif point_cardJ1 == point_cardJ2:
        if getCardColor(card_file,str(cardJ1)) == atout:
            gagnant = 0
            points = point_cardJ1
        elif getCardColor(card_file,str(cardJ2)) == atout:
            gagnant = 1
            points = point_cardJ2
        else:
            gagnant = None
            points = 0  
        
    return gagnant,points
        
    
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

def getCardValue(fic:str,img_name:str):
    """Renvoi la valeur de la carte en fonction du filename de l'image

    Args:
        fic (str): fichier .csv contenant les valeurs des cartes et les noms des images
        img_name (str): Nom du fichier img de la carte recherchée

    Returns:
        str: valeur de la carte ('1' à '32')
    """
    if img_name == None:
        valeur = None
        return valeur

    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['file'] == img_name:
                valeur = card.get('Valeur')

    return valeur

def getCardFigure(fic:str, valeur:str):
    """Renvoit la figure de la carte en fonction de sa "valeur"

    Args :
        fic (str): fichier .csv contenant les valeurs des cartes et les noms des images
        valeur (int): valeur de la carte (1 à 32)

    Returns :
        figure (str): figure de la carte ('As','Roi','Dame','Valet','10' ...)
    """
    if str(valeur) == None:
        figure = None
        return figure

    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['Valeur'] == valeur:
                figure = card.get('Figure')
    
    return figure

def getCardImg(fic: str, valeur: str):
    """Renvoit le filename de l'image en fonction de la valeur de la carte
    
    Args:
        fic (str): fichier .csv contenant les valeurs des cartes et les noms des images
        valeur (int): valeur de la carte (1 à 32)
    
    Returns:
        imgName (str) : nom du fichier de l'image correspondant à la carte
    """
    if valeur == str(None):
        image = None
        return image
    
    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['Valeur'] == valeur:
                imgName = card.get('file')

    return imgName

def getCardColor(fic: str,valeur: str):
    """Renvoi la couleur d'une carte en fonction de sa valeur
    
    Args:
        valeur (str) : Valeur de la carte (1 à 32)
    
    Returns:
        couleur (str): Renvoit la couleur de la carte entrée
    """
    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['Valeur'] == valeur:
                couleur = card.get('Couleur')

    return couleur

def startingPlayer():
    """Determine le joueur commençant la partie
    
    Returns:
        joueur (int) : Renvoit le numéro du joueur commençant la partie (0,1)
    """
    joueur = random.randint(0,1)
    return joueur

def saveGame(save_fic: str, donne:tuple, pli:list, joueur:list ,atout:str, score:list):
    """Sauvegarde les données de la parties en cours dans un fichier gameData

    Args:
        save_fic (str): chemin d'enregistrement du fichier
        donne (tuple): donne complète de la partie en cours
        pli (list): n° du pli
        joueur (list): joueur ayant la main
        atout (str): atout de la partie
        score (list): scores de la partie
    """
    save_file = open(save_fic,'w')
    save_data = [donne, pli, joueur, atout, score]
    save_file.write(str(save_data))
    save_file.close()

def loadGame(save_fic):
    """Charge les données de la partie sauvegardée

    Args:
        save_fic (str): chemin du fichier de sauvegarde

    Returns:
        tuple: (donne, pli, joueur, atout)
    """
    load_file = open(save_fic,'r')
    game_data = ast.literal_eval(load_file.read())
       
    return game_data

def cards_points(fic, atout:str, valeur:int):
    """Détermine les points de la carte selon l'atout

    Args:
        fic (str): fichier .csv contenant les valeurs des cartes et les noms des images
        atout (str): atout de la partie
        valeur (int): valeur de la carte selon (1 à 32)

    Returns:
        int: points de la carte
    """
    
    figure = getCardFigure(fic, str(valeur))
    Couleur=getCardColor(fic, str(valeur))
    if Couleur == atout :
        if figure == 'As':
            points =11
        if figure == 'Roi':
            points =4
        if figure == 'Dame':
            points=3
        if figure == 'Valet':
            points =20
        if figure == '10':
            points =10
        if figure == '9':
            points =14
        if figure == '8':
            points = 0
        if figure == '7':
            points =0
    else:
        if figure == 'As':
            points =11
        if figure == 'Roi':
            points =4
        if figure == 'Dame':
            points=3
        if figure == 'Valet':
            points =2
        if figure == '10':
            points =10
        if figure == '9':
            points = 0
        if figure == '8':
            points = 0
        if figure == '7':
            points =0
    
    return points

