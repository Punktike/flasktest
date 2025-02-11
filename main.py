from flask import Flask, render_template
from stuff import Idea, Category

app = Flask(__name__)

@app.route('/')
def initial_page():
    # I need to figure out how to make these imports better
    a = Idea.Idea(Category.Categories.all)
    b = a.getidea()
    currentcategory : str = a.category.name
    return render_template('index.html', idea =b, currentcategory = currentcategory)

# Should maybe replace WithBack.html with a python function?
@app.route('/outdoors')
def outdoors():
    a = Idea.Idea(Category.Categories.outdoors)
    b = a.getidea()

    currenthref = "/outdoors"
    currentcategory: str = a.category.name

    return render_template('WithBack.html', idea =b, currenthref = currenthref, currentcategory = currentcategory)

@app.route('/indoors')
def indoors():
    a = Idea.Idea(Category.Categories.indoors)
    b = a.getidea()

    currenthref = "/indoors"
    currentcategory: str = a.category.name

    return render_template('WithBack.html', idea =b, currenthref = currenthref, currentcategory = currentcategory)

if __name__ == "__main__":
    app.run(host='0.0.0.0',	port=3000)