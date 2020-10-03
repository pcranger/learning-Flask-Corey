from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'd4321de9660ff96c2eeba731cbe3df92'

posts = [
    {
        'author': 'Tran Minh Hieu',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'Sep 20 2020'
    },
    {
        'author': 'Tran Minh ',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'Sep 20 2020'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts = posts)

@app.route("/about")
def about():
    return render_template('about.html',title = 'About')

@app.route("/register", methods = ['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit()
        flash(f'Account created for {form.username.data}!', 'success') #success is a bootstrap class
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form = form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title = 'Register', form = form)



if __name__ == '__main__':
    app.run(debug =True)