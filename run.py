from flask import Flask, render_template, request, session
import fonctions

card_file = 'static/cards/cards.csv'

app = Flask(__name__)

donne = fonctions.init_game()

mt_line = ["carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png","carte_0.png"]



donneIMG = (donne[0], donne[2],mt_line,donne[3],donne[1])

@app.route('/')
def index():
    #for i in range(0,7):
        #table_liste = [mainJ1_IMG[i],cacheJ1_IMG[i],None,cacheJ2_IMG[i],mainJ2_IMG[i]]

    return render_template('belote.html', donne = donneIMG)


if __name__=='__main__':
    app.secret_key = "teobubu"
    app.run(debug='True')

