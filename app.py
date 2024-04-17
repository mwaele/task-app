from flask import Flask

# Creating a flask applicationn
app = Flask(__name__)

# Defining a route and a view
@app.route('/')
def hello_world():
    return 'Hello World!'

# Running the Flask application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)