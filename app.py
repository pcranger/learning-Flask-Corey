from flask import Flask, render_template
app = Flask(__name__)

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
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug =True)