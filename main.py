# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def hello():
#     return 'Hello, World112321!'


# @app.route('/rofls')
# def rofls():
#     return 'Hello, rofls!'


# @app.route('/user/<username>')
# def users(username):
#     return f'Hello, {username}!'

# if __name__ == '__main__':
#     app.run(port=8000, debug=True)

from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # проверка логина и пароля
        if username =='123' and password=='123':
            return 'Вы вошли в систему!'
        else:
            return 'Вы ввели неверный логин/пароль  '
    else:
        return render_template('login.html')

if __name__ == '__main__':
    app.run(port=8000, debug=True)

