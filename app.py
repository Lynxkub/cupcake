from flask import Flask, render_template, request, jsonify, redirect
from models import db, connect_db, Cupcake
from forms import AddCupcakeForm
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/', methods = ['GET', 'POST', 'PATCH'])
def home_page():
    cupcakes = Cupcake.query.all()

    form  = AddCupcakeForm()

  

    if request.method == 'POST':
        data = request.json
        cupcake = Cupcake(flavor = data['flavor'], rating = data['rating'], size = data['size'], image = data['image'] or None)
        
        db.session.add(cupcake)
        db.session.commit()
        return redirect('/')
    
   

    else: 
        return render_template('home.html', cupcakes = cupcakes, form = form)

@app.route('/api/cupcakes')
def get_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized = [Cupcake.serialize(cupcake) for cupcake in cupcakes]
    print(jsonify(serialized))
    return jsonify(cupcakes = serialized)

@app.route('/api/cupcakes/<int:id>')
def get_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    serialized = Cupcake.serialize(cupcake)
    return jsonify(cupcakes = serialized)

@app.route('/api/cupcakes', methods = ['POST'])
def create_cupcake():
    flavor = request.form['flavor']
    size = request.form['size']
    rating = request.form['rating']
    image = request.form['image']
    new_cupcake = Cupcake(flavor = flavor, size = size, rating = rating, image = image)
    print(new_cupcake)
    db.session.add(new_cupcake)
    db.session.commit()

    serialized = Cupcake.serialize(new_cupcake)

    return (jsonify(cupcake = serialized), 201)

@app.route('/api/cupcakes/<int:id>', methods = ['PATCH'])
def edit_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    data = request.json
    cupcake.flavor = data['flavor']
    cupcake.size = data['size']
    cupcake.rating = data['rating']
    cupcake.image = data['image']

    db.session.commit()
    return redirect('/')
    # return jsonify(cupcake = Cupcake.serialize())

@app.route('/api/cupcakes/<int:id>', methods = ['DELETE'])
def delete_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message = 'deleted')

@app.route('/edit_cupcake<int:id>')
def edit_cupcake_page(id):
    cupcake = Cupcake.query.get_or_404(id)
    form = AddCupcakeForm(obj = cupcake)

    # if form.validate_on_submit():
    #     redirect(f'/api/cupcakes/{id}')

    # else:
    return render_template('edit_cupcake.html', form = form, cupcake = cupcake)

