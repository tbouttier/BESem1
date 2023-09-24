
import os
from flask import Flask, render_template, request, flash, redirect, send_file
from werkzeug.utils import secure_filename

import fonctions


"""
Note : joueur et pli sont des listes à 1 seul élément (int) afin de contourner le problème des entiers immutable dans les fonctions 
"""

UPLOAD_FOLDER = 'saves/'
ALLOWED_EXTENSIONS = {'bel'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

card_file = 'static/cards/cards.csv'

app = Flask('__main__')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():

    return render_template('testindex.html')

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
        
    return redirect('/game')


@app.route('/game')
def game():
    fonctions.checkTapis(donne[2][0],donne[3][0],atout,score,joueur,pli)
    if pli[0] < 16:
        fonctions.saveGame('saves/gameData.bel',donne,pli,joueur,atout,score)
    return render_template('game.html', donne = donne, joueur = joueur[0], atout = atout,score=score,pli = pli[0])

@app.route('/j1/<card>')
def jeu_j1(card):
    fonctions.cardPlayed(donne[0],donne[1],donne[2],donne[0][int(card)-1]['valeur'],int(card))
    joueur[0]+=1
    
    return redirect('/game')


@app.route('/j2/<card>')
def jeu_j2(card):
    fonctions.cardPlayed(donne[5],donne[4],donne[3],donne[5][int(card)-1]['valeur'],int(card))
    joueur[0]-=1

    
    return redirect('/game')

@app.route('/loadGame', methods=['GET', 'POST'])
def loadGame():
    if request.method == 'POST':
        if 'save' not in request.files:
            flash('Fichier innaproprié')
            
            return redirect('/loadGame')
        file = request.files['save']
        if file.filename == '':
            flash('No selected file')
            return redirect('/loadGame')
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        
            global donne,atout,joueur,score,pli
            gameData = fonctions.loadGame(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            donne = gameData[0]
            pli = gameData[1]
            joueur = gameData[2]
            atout = gameData[3]
            score = gameData[4]
        
            return redirect('/game')
    
    else: return render_template('load.html')

@app.route('/download')
def Download_Save():
    PATH = 'saves/gameData.bel'
    return send_file(PATH, as_attachment=True)

@app.route('/j2/<card>')
def jeu_j2(card):
    fonctions.cardPlayed(0,donne[5],donne[4],donne[3],donne[5][int(card)-1]['valeur'],int(card))
    global tour
    tour-=1
    
    return redirect('/game')
    

if __name__=='__main__':
    app.secret_key = "teobubu"
    app.run(debug='True')
