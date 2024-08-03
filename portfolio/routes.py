from flask import render_template, request
from portfolio import app

from markdown_it import MarkdownIt
md = MarkdownIt()

import os

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

@app.route('/postsContent/<blog_name>')
def postsContent(blog_name):
    blog_path = os.path.join('./portfolio/blogs', f'{blog_name}.md')
    if not os.path.exists(blog_path):
        render_template('errors.html')

    with open(blog_path, 'r') as blog_file:
        blog_content = blog_file.read()
    
    html_content = md.render(blog_content)
    return render_template('postsContent.html', title ="posts", content= html_content)





# For emails 
@app.route('/sent', methods=['POST', 'GET'])
def sent():
    pass