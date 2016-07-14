from flask import Flask, render_template, request
import httplib2
import json

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')


@app.route('/daily-bible-verse')
def daily_bible_verse():
    
    http = httplib2.Http()
    url = "http://www.ourmanna.com/verses/api/get/?format=json"
    
    if request.args.get('random', None) is not None:
        url += "&order=random"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
               'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
    
    print("getting a new verse in ourmanna.com")
    
    (response, content) = http.request(url, method="GET", headers=headers)
    
    print("prossesing the verse")
    
    json_data = json.loads(content)
    
    verse_text = json_data['verse']['details']['text']
    verse_reference = json_data['verse']['details']['reference']
    
    return render_template('daily_bible_verse.html', verse=verse_text, reference=verse_reference)
    
if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)