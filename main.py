from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def initial_page():
    return render_template('index.html')

if __name__ == "__main__": #Why does name have to be __main__?
    app.run(host='0.0.0.0',	port=3000)