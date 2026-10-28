from flask import Flask, request, jsonify, render_template
from antlr4 import InputStream
from analizar import parsear, ErrorBazilio
from BazilioParser import BazilioParser

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analizar", methods=["POST"])
def ejecutar():
    codigo = request.json.get("codigo", "")

    try:
        # 1. Convertimos el string recibido en un flujo de ANTLR4
        flujo = InputStream(codigo)
        
        # 2. Usamos la función parsear que ya existe en tu analizar.py
        arbol = parsear(flujo)
        
        resultado = {
            "estado": "exito",
            "mensaje": "Sintaxis correcta",
            "arbol": arbol.toStringTree(ruleNames=BazilioParser.ruleNames)
        }
    except ErrorBazilio as e:
        # 3. Capturamos los errores de sintaxis personalizados de tu archivo
        resultado = {
            "estado": "error",
            "mensaje": str(e)
        }

    return jsonify(resultado)

if __name__ == "__main__":
    app.run()
