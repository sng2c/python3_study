from flask import Flask
from flask import request, redirect, current_app
import datetime
import hashlib

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

    # 글자 md5 시키기
    # $ python3
    # Python 3.5.1 (default, May 20 2016, 18:18:52)
    # [GCC 4.2.1 Compatible Apple LLVM 7.3.0 (clang-703.0.31)] on darwin
    # Type "help", "copyright", "credits" or "license" for more information.
    # >>> import hashlib
    # >>> hashlib.md5("1111".encode()).hexdigest()
    # 'b59c67bf196a4758191e42f76670ceba'

    userpw = hashlib.md5(userpw.encode()).hexdigest()

    login_ok = False

    with open("passwords.txt") as passfile:
        for passwd in passfile:
            _id, _pw = passwd.rstrip().split(":")
            if userid == _id and userpw == _pw:
                login_ok = True
                break

    if login_ok:
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
