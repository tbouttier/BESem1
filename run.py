from flask import Flask, render_template, request, session

app = Flask(__name__)








if __name__=='__main__':
    app.secret_key = "teobubu"
    app.run(debug='True')