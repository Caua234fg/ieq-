from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/horarios")
def horarios():
    return render_template("horarios.html")

@app.route("/endereco")
def endereco():
    return render_template("endereco.html")


@app.route("/pedidos", methods=["GET", "POST"])
def pedidos():
    if request.method == "POST":
        mensagem = request.form.get("mensagem")
        with open("pedidos.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(mensagem + "\n" + "-"*40 + "\n")
        return render_template("pedidos.html", enviado=True)
    return render_template("pedidos.html", enviado=False)

@app.route("/admin", methods=["GET", "POST"])
def admin():
    senha_correta = "oracao123"  # você pode trocar por outra senha
    if request.method == "POST":
        senha = request.form.get("senha")
        if senha == senha_correta:
            try:
                with open("pedidos.txt", "r", encoding="utf-8") as arquivo:
                    pedidos = arquivo.read()
            except FileNotFoundError:
                pedidos = "(Nenhum pedido encontrado)"
            return render_template("admin.html", pedidos=pedidos)
        else:
            erro = "Senha incorreta!"
            return render_template("login_admin.html", erro=erro)
    return render_template("login_admin.html", erro=None)

@app.route("/apagar", methods=["POST"])
def apagar():
    try:
        with open("pedidos.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("")  # esvazia o arquivo
        mensagem = "Todos os pedidos foram apagados com sucesso!"
    except Exception as e:
        mensagem = f"Ocorreu um erro ao apagar: {e}"

    return render_template("admin_apagado.html", mensagem=mensagem)


if __name__ == "__main__":
    app.run(debug=True)
