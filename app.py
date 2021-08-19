import sqlite3
from flask import Flask, request, session, g, redirect, abort, render_template, flash

# configurações
DATABASE = "blog.db"
SECRET_KEY = 'pudim'


app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/hello')
def pagina_inicial():
    return "Hello World"
