from flask import Flask 

app = Flask(__name__) # Flask 객체를 생성한다 
                      #생성자에서 파일명을 받아간다 
                      #__name__ 를 매개변수로 전달해야 한다 

#데코레이터 - @ 함수나 클래스를 만들어서 다른 함수르 납치해와서 
#기능을 부여할 수 있다 

@app.route("/")  #라우트(경로배정) - 이문구가 지정된 함수는 라우터로 
                 #사용한다. 
def index():
    return "<h1 style='color:blue'>Hello, Flask</h1>"

#http://127.0.0.1:7000/hello
@app.route("/hello")  
def hello():
    return "<h3>Hi Hello</h3>"

#http://127.0.0.1:7000/hello2/홍길동
@app.route("/hello2/<username>")
def hello2(username):
    return f"Hello {username}"

#http://127.0.0.1:7000/add/4/5
@app.route("/add/<int:x>/<int:y>")
def add(x, y):
    #x = int(x)
    #y = int(y) 
    return f"<h3 style='color:green'>{x} + {y} = {x+y}</h3>"

#http://127.0.0.1:7000/sub/4/5
@app.route("/sub/<int:x>/<int:y>")
def sub(x, y):
    return f"{x} - {y} = {x-y}"

#http://127.0.0.1:7000/gugudan/4
@app.route("/gugudan/<int:dan>")
def gugudan(dan):
    result = "" #전체 문자열 하나가 클라이언트로 전달되어야 한다 
    for i in range(1, 10):
        result += f"<strong>{dan} X {i} = {dan*i}</strong><br/>"
    return result 

#http://127.0.0.1:7000/star/8
@app.route("/star/<int:cnt>")
def star(cnt):
    result=""
    for i in range(1, cnt+1):
        for j in range(1, cnt-i+1):
            result=result+"&nbsp;"
            
        for j in range(1, 2*i):
            result=result+"*"
        result = result + "<br/>"

    #기둥그리기 
    for i in range(1, 5):
        start = (cnt*2-1)//2-3
        end = (cnt*2-1)//2 + 3
        for j in range(1, start+1):
            result = result + "&nbsp;"
        for j in range(start, end+1):
            result = result + "*"
        result = result + "<br/>"
        
    return result 

            
         






if __name__ == "__main__":
    app.run('0.0.0.0', port=7000)  #서버 시작 
    #python server1.py 
    #0.0.0.0 - 현재 서버가 작동중인 컴푸터 아이피를 사용하라 