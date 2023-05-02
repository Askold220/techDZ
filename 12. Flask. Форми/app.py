from flask import Flask, render_template, request

app = Flask(__name__)


class Optional(object):
    def __call__(self, form, field):
        if not field.data:
            field.errors[:] = []
            raise StopIteration()


class RegistrationForm(object):
    def __init__(self, name=None, email=None, password=None):
        self.name = name
        self.email = email
        self.password = password


@app.route('/', methods=['GET', 'POST'])
def registration_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        registration_form = RegistrationForm(name, email, password)
        return render_template('registration_form.html', form=registration_form)

    return render_template('registration_form.html')


if __name__ == '__main__':
    app.run(debug=True)
