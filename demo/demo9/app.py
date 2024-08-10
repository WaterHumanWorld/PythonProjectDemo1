from flask import Flask, render_template

app = Flask(__name__, template_folder='D:\PythonProject\PythonProjectDemo1\demo\demo9')


@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
