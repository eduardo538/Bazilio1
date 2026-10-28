from flask import Flask, request, jsonify, render_template
from analizar import analizar

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analizar", methods=["POST"])
def ejecutar():
    codigo = request.json["codigo"]

    resultado = analizar(codigo)

    return jsonify(resultado)

if __name__ == "__main__":
    app.run()