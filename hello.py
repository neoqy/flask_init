import os # only needed in cloud 9

from flask import Flask, url_for, request
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/login', methods=['GET'])
def login():
    if request.values:
        return 'username is ' + request.values["username"]
    else:
        return '<form method="get" action="/login"><input type="text" name="username" /><p><button type="submit">Submit</button></form>'

@app.route('/username/<username>')
def show_user_profile(username):
    return 'User ' + str(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post ' + str(post_id)

@app.route('/hello')
def hello_world():
    return 'Hello World!'
    
@app.route('/show_url')
def show_url():
    return url_for('show_user_profile', username='Ouyang')
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0') # only needed in cloud 9
    port = int(os.getenv('PORT', 5000)) # only needed in cloud 9
    app.debug = True
    app.run(host=host, port=port)
