from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, TelField, IntegerField, RadioField

from wtforms import validators, ValidationError
from wtforms.validators import ValidationError


class PuntosForm(FlaskForm):
    x1 = IntegerField('x1')
    x2 = IntegerField('x2')
    y1 = IntegerField('y1')
    y2 = IntegerField('y2')
    resultado = IntegerField('resultado')

class ColoresForm(FlaskForm):
    primeraBanda= IntegerField('primeraBanda')
    segundaBanda= IntegerField('segundaBanda')
    terceraBanda= IntegerField('terceraBanda')
    tolerancia= IntegerField('tolerancia')
    valor= IntegerField('valor')
    valorMaximo= IntegerField('valorMaximo')
    valorMinimo= IntegerField('valor')

class RegistrarColores(Form):
    colorIngles = StringField('colorIngles', [validators.DataRequired(message='El campo color en Ingles es requerido'),
                                               validators.Length(min=3, max=10, message='Ingresa un color valido')])
    colorEspanol = StringField('colorEspanol', [validators.DataRequired(message='El campo color en Español es requerido'),
                                                 validators.Length(min=3, max=10, message='Ingresa un color valido')])

def validate_seleccionarColor(form, field):
    if not field.data:
        raise ValidationError('Debe seleccionar un idioma.')

class BuscarColores(Form):
    buscarColor = StringField('buscarColor', [validators.DataRequired(message='El campo para buscar es requerido'),
                                               validators.Length(min=3, max=10, message='Ingresa un color valido')])
    seleccionarColor = RadioField('Idioma', choices=[('ingles', 'Ingles'), ('espanol', 'Espanol')],
                                  validators=[validate_seleccionarColor], coerce=str)
                                  
    
