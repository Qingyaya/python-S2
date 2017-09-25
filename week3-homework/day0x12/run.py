#-*- coding:utf-8 -*-

from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def hello_world():
	file = open('test.json','r+')
	file_text=file.read()
	file_text = dict(json.loads(file_text))
	return render_template('real.html',data=file_text)

if __name__ == '__main__':
    app.run(debug=True)