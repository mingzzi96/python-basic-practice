# 필수 라이브러리
'''
0. Flask : 웹서버를 시작할 수 있는 기능. app이라는 이름으로 플라스크를 시작한다
1. render_template : html파일을 가져와서 보여준다
'''
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def home():
    name = '권지민'
    motto = '행복해서 웃는게 아니라, 웃어서 행복합니다.'
    context = {
        "name": name,
        "motto": motto
    }
    return render_template('motto.html', data=context)

@app.route("/music")
def music():
    return render_template('music.html')

@app.route("/iloveyou/<name>")
def iloveyou(name):
    motto = f"{name}야 사랑해!"
    context = {
        "name": name,
        "motto": motto
    }
    return render_template('motto.html', data=context)


if __name__ == "__main__":
    app.run(debug=True)