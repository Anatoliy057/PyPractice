import re

from flask import Flask, redirect, url_for, render_template, request
import urllib.request

app = Flask(__name__)


@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/')
def main():
    return redirect('/index')


@app.route('/index', methods=['POST'])
def search():
    url = request.form['url']
    return redirect(url_for(endpoint='scan', args=url))


@app.route('/scanner', methods=['GET'])
def scan():
    try:
        response = urllib.request.urlopen(request.args['args'])
    except ValueError:
        return redirect('index')
    html = response.read().decode('utf-8')
    result = {}
    parts = re.split(r'<[^>]*>', html)
    for part in parts:
        group = re.split(r'[\->@%_\r\t\n,!?.:; (){}\\|/=\[\]\"\'#&0-9]', part)
        for s in group:
            if s == '':
                continue
            if s not in result:
                result[s] = 1
            else:
                result[s] = result[s] + 1

    def sort(item):
        return item[1]
    return render_template('result.html', words=sorted(result.items(), key=sort, reverse=True))


app.run()
