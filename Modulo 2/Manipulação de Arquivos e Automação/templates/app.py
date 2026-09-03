from flask import Flask, render_template, request, redirect, url_for 
import sqlite3

app = Flask(__name__)

BANCO = 'jogos.db'

def conectar():
    conexao = sqlite3.connect(BANCO)
    conexao.row_factory = sqlite3.Row
    return conexao

def criar_tabela():
    conexao = conectar()

    conexao.execute("""
    CREATE TABLE IF NOT EXISTS jogos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    genero TEXT NOT NULL,
    nota REAL NOT NULL,
    imagem_url TEXT
    )
    """)

    conexao.commit()
    conexao.close()

@app.route("/")
def index():
    conexao = conectar()
    jogos = conexao.execute("SELECT * FROM jogos ORDER BY id DESC").fetchall()
    conexao.close()

    return render_template("index.html", jogos=jogos)


@app.route("/cadastrar", methods=["POST"])
def cadastrar():
    nome = request.form["nome"]
    genero = request.form["genero"]
    nota = request.form["nota"]
    imagem = request.form["imagem_url"]

    conexao = conectar()

    conexao.execute("""
    INSERT INTO jogos (nome, genero, nota, imagem_url) VALUES (?,?,?,?)
    """, (nome,genero,nota,imagem))


    conexao.commit()
    conexao.close()


    return redirect(url_for("index"))



@app.route("/editar/<int:id>")
def editar(id):
    conexao = conectar()


    jogo = conexao.execute(
        "SELECT * FROM jogos WHERE id = ?",
        (id,)
    ).fetchone()


    conexao.close()


    return render_template("editar.html", jogo=jogo)



@app.route("/atualizar/<int:id>", methods=["POST"])
def atualizar(id):
    nome = request.form["nome"]
    genero = request.form["genero"]
    nota = request.form["nota"]
    imagem_url = request.form["imagem_url"]


    conexao = conectar()


    conexao.execute(
        """
        UPDATE jogos
        SET nome = ?, genero = ?, nota = ?, imagem_url = ?
        WHERE id = ?
        """,
        (nome, genero, nota, imagem_url, id)
    )


    conexao.commit()
    conexao.close()


    return redirect(url_for("index"))



@app.route("/excluir/<int:id>", methods=["POST"])
def excluir(id):
    conexao = conectar()


    conexao.execute(
        "DELETE FROM jogos WHERE id = ?",
        (id,)
    )


    conexao.commit()
    conexao.close()


    return redirect(url_for("index"))



criar_tabela()
app.run(debug=True)