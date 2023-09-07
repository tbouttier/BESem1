from flask import Flask, render_template, request, session
import fonctions

card_file = 'static/cards/cards.csv'

app = Flask(__name__)
mainJ1_IMG = []
mainJ2_IMG = []
cacheJ1_IMG = []
cacheJ2_IMG = []

donne = fonctions.distribCards()
mainJ1= donne[0]
mainJ2= donne[1]
cacheJ1 = donne[2]
cacheJ2 = donne[3]

for card in mainJ1:
        mainJ1_IMG.append(fonctions.getCardImg(card_file,str(card)))
for card in mainJ2:
        mainJ2_IMG.append(fonctions.getCardImg(card_file,str(card)))
for card in cacheJ1:
        cacheJ1_IMG.append(fonctions.getCardImg(card_file,str(card)))
for card in cacheJ2:
    cacheJ2_IMG.append(fonctions.getCardImg(card_file,str(card)))

@app.route('/')
def index():
    for i in range(0,7):
        table_liste = [mainJ1_IMG[i],cacheJ1_IMG[i],None,cacheJ2_IMG[i],mainJ2_IMG[i]]

    return render_template('belote.html', donne = table_liste)




if __name__=='__main__':
    app.secret_key = "teobubu"
    app.run(debug='True')

