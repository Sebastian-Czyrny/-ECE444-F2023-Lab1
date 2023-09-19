from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Regexp

# initialize the app
app = Flask(__name__)

# initialize extensions
moment = Moment(app)
bootstrap = Bootstrap(app)

# Flask-WTF config
app.config['SECRET_KEY'] = '3123N12K3NOD12N3IJ12CJIK123CNL12N3'


@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    email = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''

        email = form.email.data
        form.email.data = ''
    return render_template('index.html', form=form, name=name, email=email)

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    email = StringField("What is your UofT Email address?", validators=[DataRequired(), 
                                                                            Regexp('.*utoronto\.ca.*', 0, 'Email must be a UofT email address')])
    submit = SubmitField('Submit')

