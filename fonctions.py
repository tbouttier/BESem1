import csv
import random


def createCards():
    """
    Crée une liste de valeur des cartes de 1 à 32
    :return: list cards
    """
    cards = []
    for value in range(1, 32):
        cards.append(value)
    return cards


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


def distribCards(cards : list):
    """
    Mélange et distribue les cartes aux joueurs
    """
    random.shuffle(cards)
