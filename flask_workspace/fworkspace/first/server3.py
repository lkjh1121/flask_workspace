from flask import Flask 
from flask import request, render_template 


app = Flask(__name__) # Flask 객체를 생성한다 
                      #생성자에서 파일명을 받아간다 
                      #__name__ 를 매개변수로 전달해야 한다 

#데코레이터 - @ 함수나 클래스를 만들어서 다른 함수르 납치해와서 
#기능을 부여할 수 있다 

@app.route("/")  #라우트(경로배정) - 이문구가 지정된 함수는 라우터로 
                 #사용한다. 
def index():
    return "Hello, Flask"


#데이터를 GET방식으로 받기  methods=['GET'] GET방식으로 데이터를 
#처리한다
#http://127.0.0.1:7000/add?x=5&y=7 
@app.route("/add", methods=['GET'])
def add():
    x = int(request.values['x']) 
    y = int(request.values['y'])

    return f"{x} + {y} = {x+y}"

#http://127.0.0.1:7000/hello?name=홍길동&age=12 
#홍길동님은 12살입니다.  결과가 나오도록 프로그램하기 
@app.route("/hello", methods=['GET'])
def hello():
    name = request.values['name']
    age = request.values['age']
    return f"{name}님은 {age}살입니다"

#http://127.0.0.1:7000/rectangle?width=5&height=7
@app.route("/rectangle", methods=['GET'])
def rectangle():
    width = int(request.values['width'])
    height = int(request.values['height'])
    return f"면적은 {width*height} 입니다"

#http://127.0.0.1:7000/calc?x=5&y=9&oper=2
@app.route("/calc", methods=['GET'])
def calc():
    x = int(request.values['x'])
    y = int(request.values['y'])
    oper = request.values['oper']
    if oper=='1':
        return f"{x} + {y} = {x+y}"
    elif oper=='2':
        return f"{x} - {y} = {x-y}"
    elif oper=='3':
        return f"{x} * {y} = {x*y}"
    else:
        return f"{x} / {y} = {x/y}"
        

@app.route("/hello2", methods=['POST'])
def hello2():
    name = request.form['name']
    age = request.form['age']
    return f"{name}님은 {age}살입니다"

@app.route("/logon", methods=['POST'])
def logon():
    userid = request.form['userid']
    password = request.form['password']
    if userid=="test" and password == "1234":
        return "success"
    else:
        return "fail"




if __name__ == "__main__":
    app.run('0.0.0.0', port=7000)  #서버 시작 
    #python server1.py 
    #0.0.0.0 - 현재 서버가 작동중인 컴푸터 아이피를 사용하라 