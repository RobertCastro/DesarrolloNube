from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola, mundo! Esta es la aplicación Flask en desarrollo.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
