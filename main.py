from flask import Flask, render_template, request
from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/OperasBass")
def operas():
    return render_template("OperasBass.html")

@app.route("/resultado", methods=["GET", "POST"])
def resul():
    if request.method == "POST":
        num1 = request.form.get("n1")
        num2 = request.form.get("n2")
        operacion = request.form.get("operacion")

        if operacion == "Suma":
            return "La Suma de {} + {} = {}".format(num1, num2, str(int(num1) + int(num2)))
        elif operacion == "Resta":
            return "La Resta de {} - {} = {}".format(num1, num2, str(int(num1) - int(num2)))
        elif operacion == "Multiplicacion":
            return "La Multiplicacion de {} x {} = {}".format(num1, num2, str(int(num1) * int(num2)))
        elif operacion == "Division":
            if int(num2) != 0:
                return "La Division de {} / {} = {}".format(num1, num2, str(int(num1) // int(num2)))
            else:
                return "Error: No se puede dividir por cero."
        else:
            return "Operación no válida."
        
@app.route("/static/bootstrap/css/<path:filename>")
def send_css(filename):
    return send_from_directory(os.path.join(app.root_path, 'static', 'bootstrap', 'css'), filename, mimetype='text/css')



if __name__ == "__main__":
    app.run(debug=True)