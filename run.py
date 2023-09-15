from flask import Flask, render_template, request, session
import fonctions
import random

card_file = 'static/cards/cards.csv'

app = Flask(__name__)
mainJ1_IMG = []
mainJ2_IMG = []
cacheJ1_IMG = []
cacheJ2_IMG = []

donne = fonctions.init_game()

tapis1 = ["carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png"]
tapis2 = ["carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png"]


donneIMG = (donne[0], donne[2],tapis1,tapis2,donne[3],donne[1])

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/game')
def game():

    donneIMG = (mainJ1_IMG, cacheJ1_IMG,mt_line,cacheJ2_IMG,mainJ2_IMG)
    return render_template('belote.html', donne = donneIMG)



if __name__=='__main__':
    app.secret_key = "teobubu"
    app.run(debug='True')

