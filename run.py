from flask import Flask, render_template, request, session, redirect
import fonctions


card_file = 'static/cards/cards.csv'

app = Flask('__main__')

#Détermine qui joue


@app.route('/')
def index():

    return render_template('testindex.html')

@app.route('/game')
def game():
    global joueur
    fonctions.checkTapis(donne[2][0],donne[3][0],atout,score,joueur,pli)
    return render_template('game.html', donne = donne, joueur = joueur[0], atout = atout,score=score,pli = pli)

@app.route('/j1/<card>')
def jeu_j1(card):
    fonctions.cardPlayed(donne[0],donne[1],donne[2],donne[0][int(card)-1]['valeur'],int(card))
    global joueur
    joueur[0]+=1
    
    return redirect('/game')


@app.route('/j2/<card>')
def jeu_j2(card):
    fonctions.cardPlayed(donne[5],donne[4],donne[3],donne[5][int(card)-1]['valeur'],int(card))
    global joueur
    joueur[0]-=1
    
    return redirect('/game')

@app.route('/initGame')
def gameStart():
    
    #Définition des variables globales
    global mains,donne,atout,joueur,tapis1,tapis2,score,pli
    
    pli = [0]
    joueur=[fonctions.startingPlayer()]
    score = [0,0]
    tapis1 = [{'valeur':None, 'image':""}]
    tapis2 = [{'valeur':None, 'image':""}]

    #Initialisation du jeu de carte
    mains = fonctions.init_game()
    donne = (mains[0],mains[2],tapis1,tapis2,mains[3],mains[1])

    if joueur[0] == 0:
        atout = fonctions.getCardColor(card_file,str(donne[0][-1]['valeur']))
    else:
        atout = fonctions.getCardColor(card_file,str(donne[-1][-1]['valeur']))
        
    print(atout)
    return redirect('/game')

if __name__=='__main__':
    app.secret_key = "teobubu"
    app.run(debug='True')
