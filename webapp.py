from flask import Flask
from flask import request, redirect, current_app
import datetime

app = Flask(__name__)


@app.route("/")
def hello():
    if "logined_userid" in request.cookies:
        return "로그인 되었습니다.<a href='/logout'>로그아웃</a>"
    return """
    <h1>로그인</h1>

    <form action="/login" method="POST">
        ID <input type="text" name="id">
        PW <input type="password" name="pw">
        <input type="submit" value="보내기">
    </form>
    """


@app.route("/login", methods=['POST'])
def login():
    userid = request.form['id']
    userpw = request.form['pw']

    if userid == "hanson" and userpw == "1111":
        # 쿠키 발급
        redirection = redirect("/")
        response = current_app.make_response(redirection)
        response.set_cookie('logined_userid', value=userid)
        return response
    else:
        return "Login FAIL"


@app.route("/logout")
def logout():
    expire_date = datetime.datetime.now()
    expire_date = expire_date + datetime.timedelta(days=-10)
    redirection = redirect("/")
    response = current_app.make_response(redirection)
    response.set_cookie('logined_userid', value="", expires=expire_date)
    return response


@app.route("/hello2")
def hello3():
    return "hello "


if __name__ == "__main__":
    app.run(debug=True)
