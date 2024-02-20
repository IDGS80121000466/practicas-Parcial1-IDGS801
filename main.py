from flask import Flask, render_template, request
from flask import Flask, render_template, request, send_from_directory
from forms import PuntosForm, ColoresForm, RegistrarColores, BuscarColores

import os
import forms
clave_secreta = os.urandom(24)

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/OperasBass")
def operas():
    return render_template("OperasBass.html")

@app.route("/colores", methods=['GET', 'POST'])
def colores():
    colorIngles = ''
    colorEspanol = ''
    buscarColor = ''
    seleccionarColor = ''
    colores_clase = RegistrarColores(request.form)
    coloress_clase = BuscarColores(request.form)
    alerta = colorEncontrado = ''
    leerEspanol = leerIngles = ''
    
    with open('coloresEspañol.txt', 'r') as archivo1:
        leerEspanol = archivo1.read()

    if request.method == 'POST':    
        if 'btn_registrar' in request.form:
            if colores_clase.validate():
                colorIngles = colores_clase.colorIngles.data
                colorEspanol = colores_clase.colorEspanol.data
                if not colorExistente('coloresEspañol.txt', colorEspanol):
                    with open('coloresEspañol.txt', 'a') as archivo1:
                        archivo1.write('\n' + colorEspanol + '\n' + colorIngles)                      
                    with open('coloresEspañol.txt', 'r') as archivo1:
                        leerEspanol = archivo1.read()
                    print('Color Español: {}'.format(colorEspanol))
                    alerta = "El color se ha registrado correctamente."
                else:
                    alerta = "El color ya está registrado."
        elif 'btn_buscar' in request.form:
            if coloress_clase.validate():
                buscarColor = coloress_clase.buscarColor.data
                seleccionarColor = coloress_clase.seleccionarColor.data
                with open('coloresEspañol.txt', 'r') as archivo1:
                        leerEspanol = archivo1.read()
                colorEncontrado = traducir_color(buscarColor, seleccionarColor)
                print('Buscar Color: {}'.format(buscarColor))
                print('Seleccionar Color: {}'.format(seleccionarColor))
    
    return render_template("colores.html", form=colores_clase, form_buscar=coloress_clase, 
                           colorIngles=colorIngles, colorEspanol=colorEspanol,
                           seleccionarColor=seleccionarColor, listaEspanol=leerEspanol, listaIngles= leerIngles, 
                           colorEncontrado = colorEncontrado, alerta=alerta)

def colorExistente(rutaArchivo, color):
    with open(rutaArchivo, 'r') as archivo:
        colores_existentes = archivo.read().splitlines()
        if color in colores_existentes:
            return True
        else:
            return False
            
def traducir_color(buscar_color, idioma):
    with open('coloresEspañol.txt', 'r', encoding='utf-8') as archivo:
        lineas = archivo.readlines()

    traducciones_espanol = {}
    traducciones_ingles = {}
    
    for i in range(1, len(lineas), 2):
        palabra_espanol = lineas[i].strip()
        palabra_ingles = lineas[i+1].strip()
        traducciones_espanol[palabra_espanol] = palabra_ingles
        traducciones_ingles[palabra_ingles] = palabra_espanol

    if idioma == 'ingles':
        if buscar_color in traducciones_espanol:
            return traducciones_espanol[buscar_color]
        elif buscar_color in traducciones_ingles:
            return buscar_color
        else:
            return "Error: Palabra no encontrada."
    elif idioma == 'espanol':
        if buscar_color in traducciones_ingles:
            return traducciones_ingles[buscar_color]
        elif buscar_color in traducciones_espanol:
            return buscar_color
        else:
            return "Error: Palabra no encontrada."
    else:
        return "Error: idioma no válido."







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

@app.route("/puntos", methods=['GET', 'POST'])
def puntos():
    x1 = x2 = y1 = y2 = ''
    puntos_clase = PuntosForm(request.form)
    if request.method == 'POST':
        x1 = puntos_clase.x1.data
        x2 = puntos_clase.x2.data
        y1 = puntos_clase.y1.data
        y2 = puntos_clase.y2.data
        
        resta1 = x2 - x1
        resta2 = y2 - y1

        distancia = (resta1 ** 2 + resta2 ** 2) ** 0.5

        puntos_clase.resultado.data = distancia

        print("La distancia entre los puntos es:", distancia)

        print('x1: {}'.format(x1))
        print('x2: {}'.format(x2))
        print('y1: {}'.format(y1))
        print('y2: {}'.format(y2))
        print('resultado: {}'.format(distancia))

    return render_template("distanciaPuntos.html", form=puntos_clase, x1=x1, x2=x2, y1=y1, y2=y2)

def obtener_color(numero):
    colores = {
        0: ("Negro", "#000000"),
        1: ("Café", "#8B4513"),
        2: ("Rojo", "#FF0000"),
        3: ("Naranja", "#FFA500"),
        4: ("Amarillo", "#FFFF00"),
        5: ("Verde", "#008000"),
        6: ("Azul", "#0000FF"),
        7: ("Morado", "#800080"),
        8: ("Gris", "#808080"),
        9: ("Blanco", "#FFFFFF")
    }
    return colores.get(numero, ("Color no definido", "#FFFFFF"))

def obtener_color2(numero):
    colores = {
        1: ("Negro", "#000000"),
        10: ("Café", "#8B4513"),
        100: ("Rojo", "#FF0000"),
        1000: ("Naranja", "#FFA500"),
        10000: ("Amarillo", "#FFFF00"),
        100000: ("Verde", "#008000"),
        1000000: ("Azul", "#0000FF"),
        10000000: ("Morado", "#800080"),
        100000000: ("Gris", "#808080"),
        1000000000: ("Blanco", "#FFFFFF")
    }
    return colores.get(numero, ("Color no definido", "#FFFFFF"))

@app.route("/resistencia", methods=['GET', 'POST'])
def resistencia():
    colores = ColoresForm(request.form)
    if request.method == 'POST':
        color1 = colores.primeraBanda.data
        color2 = colores.segundaBanda.data
        color3 = colores.terceraBanda.data
        tolerancia = colores.tolerancia.data
        rColor1 = obtener_color(color1)
        rColor2 = obtener_color(color2)
        rColor3 = obtener_color2(color3)
        rtolerancia = None

        valorMaximo = colores.valorMaximo.data
        valorMinimo = colores.valorMinimo.data

        resultadoValor = int(str(color1) + str(color2))
        resultadoValor2 = resultadoValor * color3

        tolerancia = request.form.get("tolerancia")
        if tolerancia == "0.01":
            rtolerancia = "Plata"
            rtolerancia_color = "silver"  
        elif tolerancia == "0.05":
            rtolerancia = "Oro"
            rtolerancia_color = "gold"

        if tolerancia is not None:
            try:
                resultadoValorMaximo = resultadoValor2 + (resultadoValor2 * float(tolerancia)) 
            except ValueError:
                print("Error: La tolerancia no es un número válido.")
        else:
            print("Error: El valor de tolerancia es None y no se puede convertir.")

        if tolerancia is not None:
            try:
                resultadoValorMinimo = resultadoValor2 - (resultadoValor2 * float(tolerancia)) 
            except ValueError:
                print("Error: La tolerancia no es un número válido.")
        else:
            print("Error: El valor de tolerancia es None y no se puede convertir.")

        print("Color 1:", color1)
        print("Color 2:", color2)
        print("Color 3:", color3)
        print("Tolerancia:", tolerancia)
        print("Valor:", resultadoValor)
        print("Valor Máximo:", valorMaximo)
        print("Valor Mínimo:", valorMinimo)
    else:
        colores = ColoresForm()

    return render_template("resistencia.html", form=colores, valor=resultadoValor2, valorMaximo=resultadoValorMaximo,
                           valorMinimo=resultadoValorMinimo, primeraBanda=rColor1, segundaBanda=rColor2,
                           terceraBanda=rColor3, tolerancia = rtolerancia, tolerancia_color=rtolerancia_color)

    

if __name__ == "__main__":
    app.run(debug=True)