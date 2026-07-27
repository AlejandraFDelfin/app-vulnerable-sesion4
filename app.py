from flask import Flask, request
import sqlite3

app = Flask(__name__)
DB_PASSWORD = "admin123"  # Credencial hardcodeada (SAST)

@app.route("/buscar")
def buscar():
    termino = request.args.get("q")
    conexion = sqlite3.connect("datos.db")
    # Inyeccion SQL intencional (SAST)
    consulta = "SELECT * FROM productos WHERE nombre = '" + termino + "'"
    resultado = conexion.execute(consulta)
    return str(resultado.fetchall())

@app.route("/calcular")
def calcular():
    expresion = request.args.get("expr")
    # Uso inseguro de eval (SAST)
    return str(eval(expresion))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
