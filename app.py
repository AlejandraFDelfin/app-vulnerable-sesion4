from flask import Flask, request
import sqlite3

app = Flask(__name__)

@app.route("/buscar", methods=["GET"])
def buscar():
    termino = request.args.get("q", "")
    conexion = sqlite3.connect("datos.db")
    # Corrección SAST: Uso de consultas parametrizadas contra inyección SQL
    consulta = "SELECT * FROM productos WHERE nombre = ?"
    resultado = conexion.execute(consulta, (termino,))
    return str(resultado.fetchall())

@app.route("/calcular", methods=["GET"])
def calcular():
    # Corrección SAST: Eliminación completa de eval() por lógica segura
    try:
        num1 = int(request.args.get("num1", 0))
        num2 = int(request.args.get("num2", 0))
        return str(num1 + num2)
    except ValueError:
        return "Por favor ingresa números válidos."

if __name__ == "__main__":
    # Corrección SAST: Escuchar solo en localhost de forma segura en desarrollo
    app.run(host="127.0.0.1", port=8080)
