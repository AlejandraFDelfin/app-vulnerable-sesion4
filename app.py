from flask import Flask, request, jsonify  # <-- Añade jsonify aquí
import sqlite3

app = Flask(__name__)

@app.route("/buscar", methods=["GET"])
def buscar():
    termino = request.args.get("q", "")
    conexion = sqlite3.connect("datos.db")
    
    # 1. Consulta parametrizada (Protege contra Inyección SQL)
    consulta = "SELECT * FROM productos WHERE nombre = ?"
    cursor = conexion.execute(consulta, (termino,))
     filas = cursor.fetchall()
    conexion.close()
    
    # 2. Corrección XSS: Devolver una respuesta JSON estructurada y segura
    return jsonify({"resultados": filas})

@app.route("/calcular", methods=["GET"])
def calcular():
    try:
        num1 = int(request.args.get("num1", 0))
        num2 = int(request.args.get("num2", 0))
        return jsonify({"resultado": num1 + num2})  # Seguro también aquí
    except ValueError:
        return jsonify({"error": "Por favor ingresa números válidos."}), 400

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)

