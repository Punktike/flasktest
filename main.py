from flask import Flask, render_template
from stuff import Idea, Category

app = Flask(__name__)

@app.route('/')
def initial_page():
    a = Idea.Idea(Category.Categories.all)
    b = a.getidea()
    return render_template('index.html', idea =b)

@app.route('/outdoors')
def outdoors():
    a = Idea.Idea(Category.Categories.outdoors)
    b = a.getidea()
    return render_template('index.html', idea =b)

@app.route('/indoors')
def indoors():
    a = Idea.Idea(Category.Categories.indoors)
    b = a.getidea()
    return render_template('index.html', idea =b)

if __name__ == "__main__": #Why does name have to be __main__?
    app.run(host='0.0.0.0',	port=3000)