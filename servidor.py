from flask import Flask, render_template, request, session, redirect
app=Flask(__name__)
#app.config["SECRET_KEY"]= "jogo"

class jogo:
    def __init__(self,nome,genero,ano_de_criacao):
        self.nome = nome
        self.genero = genero
        self.ano_de_criacao = ano_de_criacao

@app.route("/")
def inicio():
    return render_template("inicio.html")

@app.route("/listar_jogos")
def listar_jogos():
    return render_template("listar_jogos.html")

@app.route("/incluir_jogos")
def incluir_jogos():
    return render_template("incluir_jogos.html")
    

app.run(debug=True, host="0.0.0.0")
