from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

def conectar():
    return sqlite3.connect('database.db')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/criar', methods=['GET', 'POST'])
def criar():
    if request.method == 'POST':

        tema = request.form['tema']
        turma = request.form['turma']
        data = request.form['data']
        objetivo = request.form['objetivo']
        atividade = request.form['atividade']

        conn = conectar()
        cursor = conn.cursor()

        cursor.execute('''
        INSERT INTO planos
        (tema, turma, data, objetivo, atividade)
        VALUES (?, ?, ?, ?, ?)
        ''', (tema, turma, data, objetivo, atividade))

        conn.commit()
        conn.close()

        return redirect('/listar')

    return render_template('criar.html')

@app.route('/listar')
def listar():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM planos')

    planos = cursor.fetchall()

    conn.close()

    return render_template('listar.html', planos=planos)

if __name__ == '__main__':
    app.run(debug=True)