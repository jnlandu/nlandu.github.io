from flask import render_template, request
from portfolio import app

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="home")


@app.route('/about')
def about():
    return render_template('about.html', title="about")


@app.route('/posts')
def posts():
    return render_template('posts.html', title ="posts")

@app.route('/events')
def event():
    return render_template('events.html', title ="event")



@app.route('/contact')
def contact():
    return render_template('contact.html', title ="contact")


@app.route('/resume')
def resume():
    return render_template('resume.html', title ="resume")

@app.route('/consulting')
def consulting():
    return render_template('consulting.html', title ="consulting")

@app.route('/postsContent')
def postsContent():
    return render_template('postsContent.html', title ="posts")

# For emails 
@app.route('/sent', methods=['POST', 'GET'])
def sent():
    pass