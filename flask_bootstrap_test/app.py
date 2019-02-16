from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_nav import Nav
from flask_nav.elements import Navbar, View
from flask_wtf import FlaskForm
from wtforms.fields import SelectField, SubmitField, IntegerField

app = Flask(__name__)
bootstrap = Bootstrap(app)
nav = Nav()
nav.init_app(app)

app.config['BOOTSTRAP_SERVE_LOCAL'] = True

@nav.navigation()
def mynavbar():
    return Navbar('Test',
                  View('Foo', 'index'),
                  View('Bar', 'index'))

app.secret_key = 'my_secret_development_key'

class TestForm(FlaskForm):

    select_field = SelectField(choices=[('foo', 'foo'), ('bar', 'bar')])
    integer_field1 = IntegerField(label='Field 1')
    integer_field2 = IntegerField(label='Field 2')
    integer_field3 = IntegerField(label='Field 3')
    submit_field = SubmitField(label='Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    form = TestForm()
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
