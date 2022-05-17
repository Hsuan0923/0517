from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<name>')
@app.route('/')
def index(name=''):
    return render_template('index.html',name=name)

if __name__=='__main__':
    app.run(port=5050, debug=True)



