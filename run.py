from flask import Flask, render_template, request, session, redirect
import fonctions
import copy


card_file = 'static/cards/cards.csv'

app = Flask('__main__')

#Détermine qui joue


@app.route('/')
def index():

    return render_template('index.html')

@app.route('/game')
def game():

    return render_template('belote.html', donne = donne, joueur = joueur, atout = atout)

@app.route('/j1/<card>')
def jeu_j1(card):
    fonctions.cardPlayed(donne[0],donne[1],donne[2],donne[0][int(card)-1]['valeur'],int(card))
    global joueur
    joueur+=1
    
    return redirect('/game')


@app.route('/j2/<card>')
def jeu_j2(card):
    fonctions.cardPlayed(donne[5],donne[4],donne[3],donne[5][int(card)-1]['valeur'],int(card))
    global joueur
    joueur-=1
    
    return redirect('/game')

@app.route('/initGame')
def gameStart():
    global mains,donne,atout,joueur,tapis1,tapis2
    tapis1 = []
    tapis2 = []
    tapis1.append({'valeur':None, 'image':""})
    tapis2.append({'valeur':None, 'image':""})
    mains = fonctions.init_game()
    donne = (mains[0],mains[2],copy.copy(tapis1),copy.copy(tapis2),mains[3],mains[1])
    joueur = fonctions.startingPlayer()
    atout = fonctions.getCardColor(card_file,str(donne[joueur][-1]['valeur']))

    return redirect('/game')

if __name__=='__main__':
    app.secret_key = "teobubu"
    app.run(debug='True')
