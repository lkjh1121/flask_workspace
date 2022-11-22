from flask import Flask, redirect, session  
from flask import request, render_template 

app = Flask(__name__) # Flask 객체를 생성한다 
                      #생성자에서 파일명을 받아간다 
                      #__name__ 를 매개변수로 전달해야 한다 

#데코레이터 - @ 함수나 클래스를 만들어서 다른 함수르 납치해와서 
#기능을 부여할 수 있다 

#render_template("html 문서명", 문서에전달할데이터(dict타입))
app.secret_key="dewsdfoj2p349ru329-4ucdxz"
#세션을 암호화 해서 저장할때 사용하는 키값이다 

@app.route("/")  #라우트(경로배정) - 이문구가 지정된 함수는 라우터로 
                 #사용한다. 
def index():
    return render_template("/index.html")

#GET, POST방식 둘다 처리 
@app.route("/logon", methods=['GET', 'POST'])
def logon():
    if request.method=="GET":
        return render_template("/logon.html")
    else:
        userid = request.form["userid"]
        password = request.form["password"]

        if userid=="test" and password=="1234":
            session["userid"]=userid 
            session["username"]="홍길동"

        return redirect("/") #redirect로 페이지 이동시 alert창을 못띄우고

@app.route("/logout", methods=['GET', 'POST'])
def logout():
    session.clear()  #세션을 없애버린다 
    return redirect("/")   

if __name__ == "__main__":
    app.run('0.0.0.0', port=7000)  #서버 시작 
    #python server1.py 
    #0.0.0.0 - 현재 서버가 작동중인 컴푸터 아이피를 사용하라 