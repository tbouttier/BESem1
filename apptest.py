from flask import Flask, render_template

app = Flask(__name__)

# Sample list of items (you can replace this with your data)
items = [
    ["Item 1", "Item 2", "Item 3"],
    ["Item 4", "Item 5", "Item 6"],
    ["Item 7", "Item 8", "Item 9"],
]

@app.route('/')
def item_list():
    return render_template('disp_test.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
