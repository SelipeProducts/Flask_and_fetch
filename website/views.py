from flask import Blueprint, render_template

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

@views.route('/notes')
def notes():
  return render_template('notes.html')