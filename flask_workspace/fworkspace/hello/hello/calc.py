from flask import Blueprint, flash, g

#블루프린트 객체를 만든다. 블루프린트 객체를 통해서 __init__.py랑 연결된다. 
cp = Blueprint("calc", __name__, url_prefix="/calc")

#url_prefix="/calc" + /list 
#/board/list

@cp.route('/add/<int:x>/<int:y>')
def add(x, y):
    return f"<h1>{x} + {y} = {x+y}</h1>"



