import os # only needed in cloud 9

from flask import Flask, url_for, request, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'Hello World!'

@app.route('/username/<username>')
def show_user_profile(username):
    return 'User ' + str(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post ' + str(post_id)
    
@app.route('/show_url')
def show_url():
    return url_for('show_user_profile', username='Ouyang')

@app.route('/login_with_get', methods=['GET'])
def login_with_get():
    if request.values:
        return 'username is ' + request.values["username"]
    else:
        return '<form method="get" action="/login_with_get"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

@app.route('/login_with_post', methods=['GET', 'POST'])
def login_with_post():
    if request.method == 'POST':
        return 'username is ' + request.values["username"]
    else:
        return '<form method="post" action="/login_with_post"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'
    
@app.route('/hello_with_template')
@app.route('/hello_with_template/<name>')
def hello_with_template(name=None):
    return render_template('hello.html', name=name)
    
@app.route('/login_with_template', methods=['GET', 'POST'])
def login_with_template():
    if request.method == 'POST':
        return "User %s logged in" % request.form['username']
    return render_template('login.html')
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0') # only needed in cloud 9
    port = int(os.getenv('PORT', 5000)) # only needed in cloud 9
    app.debug = True
    app.run(host=host, port=port)
