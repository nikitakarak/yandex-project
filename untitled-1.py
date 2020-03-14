from flask import Flask, render_template
from flask import url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    a = "Миссия Колонизация Марса"
    b = "И на Марсе будут яблони цвести"
    return render_template('index.html', title='Заготовка',
                           username=a, username2=b)


@app.route('/training/<prof>')
def training(prof):
    a = "Миссия Колонизация Марса"
    b = "И на Марсе будут яблони цвести"
    c = "Чертёж больницы"
    return render_template('odd_even.html', title='127.0.0.1:8080/training/{}'.format(prof),
                           u=a, u2=b, u3=c)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
