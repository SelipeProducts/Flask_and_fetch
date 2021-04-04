from flask import Blueprint, render_template, request
from .models import Notes
from . import db

views = Blueprint('views', __name__)


@views.route('/')
def home():
  return render_template('home.html')


@views.route('/about-me')
def about_me():
  return render_template('about_me.html', name='Cesar')

@views.route('/contact')
def contact():
  return '<h1> Hello World Contact </h1>'

@views.route('/notes', methods=['GET', 'POST'])
def notes():
  notes = Notes.query

  if request.method == 'POST':
    note = request.form.get('note')

    new_note = Notes(data=note)

    db.session.add(new_note)
    db.session.commit()
  return render_template('notes.html', notes=notes)