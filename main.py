from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def mission():
    return '<h1>Миссия Колонизация Марса</h1>'


@app.route('/index')
def index():
    return '<h2>И на Марсе будут яблони цвести!</h2>'


@app.route('/promotion')
def promotion():
    return '''<p>
  Человечество вырастает из детства.
  <br>
  Человечеству мала одна планета.
  <br>
  Мы сделаем обитаемыми безжизненные пока планеты.
  <br>
  И начнем с Марса!
  <br>
  Присоединяйся!
</p>'''


@app.route('/promotion_image')
def promotion_image():
    return render_template('promotion_image.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)
