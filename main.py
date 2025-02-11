from flask import Flask, render_template
from stuff import Idea, Category

app = Flask(__name__)

@app.route('/')
def initial_page():
    a = Idea.Idea(Category.Categories.all)
    b = a.getidea()
    return render_template('index.html', idea =b)

# Should maybe replace WithBack.html with a python function?
@app.route('/outdoors')
def outdoors():
    a = Idea.Idea(Category.Categories.outdoors)
    b = a.getidea()

    currenthref = "/outdoors"

    return render_template('WithBack.html', idea =b, currenthref = currenthref)

@app.route('/indoors')
def indoors():
    a = Idea.Idea(Category.Categories.indoors)
    b = a.getidea()

    currenthref = "/indoors"
    return render_template('WithBack.html', idea =b, currenthref = currenthref)

if __name__ == "__main__":
    app.run(host='0.0.0.0',	port=3000)