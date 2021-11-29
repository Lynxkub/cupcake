from flask_wtf import FlaskForm
from wtforms import StringField, FloatField


class AddCupcakeForm(FlaskForm):
    """Add/Edit Cupcake"""

    flavor = StringField('Cupcake Flavor')
    size = StringField('Cupcake Size')
    rating = FloatField('Rating')
    image = StringField('Cupcake Image')