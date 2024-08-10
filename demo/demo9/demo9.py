from flask import Flask

app = Flask(__name__, template_folder='D:\PythonProject\PythonProjectDemo1\demo\demo9')

app.debug = True

@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)
