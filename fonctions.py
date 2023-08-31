import csv

def getCardImg(fic,valeur):
    """
    Renvoi le filename de l'image en fonction de la valeur de la carte
    """
    with open(fic, 'r') as fichier:
        cardDict = csv.DictReader(fichier, delimiter=',')
        for card in cardDict:
            if card['Valeur'] == valeur:
                imgName = card.get('file')
    
    return imgName