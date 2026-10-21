from flask import Flask
import os
import psycopg2
app = Flask(__name__)
@app.route('/')
def home():
return "He thong Quan ly chi tieu - De 38 dang chay!"
if__name__ == ' __main__':
app.run(host='0.0.0.0',port=5000)
