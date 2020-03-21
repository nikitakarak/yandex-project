from flask import Flask, render_template
from flask import url_for
import json

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
    c = "Чертёжи"
    return render_template('odd_even.html', title='127.0.0.1:8080/training/{}'.format(prof),
                           u=a, u2=b, u3=c, prof=prof)


@app.route('/list_prof/<list>')
def news(list):
    with open("news.json", "rt", encoding="utf8") as f:
        news_list = json.loads(f.read())
    print(news_list)
    return render_template('news.html', news=news_list, lis=list)


@app.route('/promotion_image')
def bootstrap():
    return '''<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="static/css/style.css" 
                    integrity="sha384-Vkoo8x4CGsO3+Hhxv8T/Q5PaXtkKtu6ug5TOeNV6gBiFeWPGFN9MuhOf23Q9Ifjh" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1 class="text-danger">Жди нас, Марс</h1>
                    <div>
                    `   <img src={} alt="здесь должна была быть картинка, но не нашлась">
                    </div>
                    <div class="p-1 mb-2 bg-primary text-light"> Человечество вырастает из детства </div>
                    <div class="p-1 mb-2 bg-success text-dark"> Человечеству мала одна планета </div>
                    <div class="p-1 mb-2 bg-primary text-light"> Мы сделаем обитаемые безжизненные пока планеты. </div>
                    <div class="p-2 mb-2 bg-warning text-dark"> И начнём с Марса! </div>
                    <div class="p-3 mb-2 bg-danger text-light"> Присоединияйся! </div>
                  </body>
                </html>'''.format("/static/img/riana2.jpg")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
