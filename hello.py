#import flask
from flask import Flask
app=Flask(__name__)
@app.route('/')
def hello_world():
    return "<h1>hello_world</h1></div><br><h2>HELLO Jeevasuriya!!!<h2>"
if __name__=='__main__':
    app.run(debug=True)
