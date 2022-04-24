from flask import Flask , request
from flask_cors import CORS
import json
app = Flask('odd_even')
CORS(app)
from even_odd import *

@app.route('/first_page',methods =['post'])
def call():
    json = request.get_json()
    # return json
    inp = json['give_input']
    r=odd_even(int(inp))
    return r
    
if __name__ == '__main__':
    app.run(debug = True)