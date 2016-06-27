from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def hello():
    return """<h1>Hello World!</h1>
    <form action="/hello" method="GET">
    name <input type="text" name="name">
    aget <input type="text" name="age">
    <input type="submit" value="보내기">
    </form>
    """


@app.route("/hello", methods=['GET', 'POST'])
def hello2():
    name = None
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = request.args.get('name')
    return "Hello " + name


@app.route("/hello2")
def hello3():
    return "hello "


if __name__ == "__main__":
    app.run(debug=True)
