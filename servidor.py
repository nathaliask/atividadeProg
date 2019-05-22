from flask import Flask, render_template, request, session, redirect
app=Flask(__name__)
app.config["SECRET_KEY"]= "jogo"
class jogo:
    def __init__(self,nome,genero,ano_de_criacao):
        self.nome = nome
        self.genero = genero
        self.ano_de_criacao = ano_de_criacao

@app.route("/")
def inicio():
    return
render_template("inicio.html")
