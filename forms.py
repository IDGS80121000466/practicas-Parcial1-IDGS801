from wtforms import Form
from flask_wtf import FlaskForm

from wtforms import StringField, TelField, IntegerField
from wtforms import EmailField

from wtforms.validators import DataRequired, Email


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
