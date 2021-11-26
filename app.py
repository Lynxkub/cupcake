from flask import Flask, render_template, request, jsonify
from models import db, connect_db, Cupcake

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/api/cupcakes')
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized = [Cupcake.serialize(cupcake) for cupcake in cupcakes]
    return jsonify(serialized)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.get_or_404(id)
    serialized = Cupcake.serialize(cupcake)
    return jsonify(serialized)