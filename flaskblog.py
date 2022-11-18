from flask import Flask, render_template
app = Flask(__name__)


posts = [
    {
        'author': 'Mahmoud Mohajer',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'Nov 10 2022'
    },
    {
    'author': 'Saeed',
    'title': 'Blog post 2',
    'content': 'second post content',
    'date_posted': 'Nov 18 2022'
    }

]






@app.route('/')
@app.route('/home')
def hello():
    return render_template('home.html', posts = posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)