import os # only needed in cloud 9

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
    
if __name__ == '__main__':
    host = os.getenv('IP', '0.0.0.0') # only needed in cloud 9
    port = int(os.getenv('PORT', 5000)) # only needed in cloud 9
    app.run(host=host, port=port)
