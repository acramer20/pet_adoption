from flask import Flask, request, redirect, render_template, flash
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "abc123"

connect_db(app)

toolbar = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    """shows homepage with list of pets, names, photos if available, and tells if the pet is available or not."""

    pets = Pet.query.all()
    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET','POST'])
def add_pet():
    """form to add pets to adoption agency"""
    form = AddPetForm()
    # depts = db.session.query(Department.dept_code, Department.dept_name)
    # form.dept_code.choices = depts
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('/add_pet.html', form = form)
@app.route('/pets/<int:id>')
def show_pet_info(id):
    """Shows page with available pet information"""
    pet= Pet.query.get_or_404(id)
    return render_template('pet_info.html', pet=pet)

@app.route('/pets/<int:id>/edit', methods=['GET', 'POST'])
def edit_pet(id):
    """shows form to edit pet"""
    pet = Pet.query.get_or_404(id)
    form = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data

        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form=form)

     