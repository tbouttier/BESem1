from flask import Flask, render_template, request, session, redirect
import fonctions
import random

card_file = 'static/cards/cards.csv'

app = Flask('__main__')
mainJ1_IMG = []
mainJ2_IMG = []
cacheJ1_IMG = []
cacheJ2_IMG = []

tapis1 = []
tapis2 = []

mains = fonctions.init_game()
donne = (mains[0],mains[2],tapis1,tapis2,mains[3],mains[1])

#Détermine qui joue
tour = fonctions.startingPlayer()


atout = fonctions.getCardColor(card_file,str(donne[tour][-1]['valeur']))


for i in range(8):
    tapis1.append({'valeur':None, 'image':"carte_0.png"})
    tapis2.append({'valeur':None, 'image':"carte_0.png"})

@app.route('/')
def index():

    return render_template('index.html')

@app.route('/game')
def game():

    return render_template('belote.html', donne = donne, tour = tour, atout =atout)

@app.route('/j1/<card>')
def jeu_j1(card):
    fonctions.cardPlayed(0,donne[0],donne[1],donne[2],donne[0][int(card)-1]['valeur'],int(card))
    global tour
    tour+=1
    
    return redirect('/game')


@app.route('/j2/<card>')
def jeu_j2(card):
    fonctions.cardPlayed(0,donne[5],donne[4],donne[3],donne[5][int(card)-1]['valeur'],int(card))
    global tour
    tour-=1
    
    return redirect('/game')
    

if __name__=='__main__':
    app.secret_key = "teobubu"
    app.run(debug='True')
