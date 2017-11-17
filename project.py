from flask import Flask, make_response, render_template, request
from verses.functions import get_verse_from_ourmanna

from whitenoise import WhiteNoise

import httplib2
import json
import os
import sys


reload(sys)
sys.setdefaultencoding("utf-8")

app = Flask(__name__)


@app.route('/daily-bible-verse')
def daily_bible_verse():
    
    random = True if request.args.get('order', None) == "random" else False
      
    (response, content) = get_verse_from_ourmanna(random)
    
    response = None
    
    if request.args.get('format', None) == "json":
            
        response = make_response(content)
        response.headers["Content-Type"]= "application/json"
        
    else:
        
        json_data = json.loads(content)
        
        verse_text = json_data['verse']['details']['text']
        verse_reference = json_data['verse']['details']['reference']
        
        return render_template('daily_bible_verse.html', verse=verse_text, reference=verse_reference)
    
    return response

if __name__ == '__main__':

    STATIC_DIR = os.path.join(os.path.dirname(__file__), "static")
    whitenoise_wrapper = WhiteNoise(app, root=STATIC_DIR, prefix='/static')

    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)