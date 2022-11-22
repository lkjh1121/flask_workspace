from flask import Blueprint, flash, g, current_app
from flask import render_template, request, redirect
from . import CommonUtil 
import os 

#current_app - app 가져다 쓰기 
#블루프린트 객체를 만든다. 블루프린트 객체를 통해서 __init__.py랑 연결된다. 
bp = Blueprint("board", __name__, url_prefix="/board")

#url_prefix="/board" + /list 
#/board/list

from .DBModule import Database

@bp.route('/list', methods=['GET', 'POST'])
def list():
    db=Database()
    sql = """
        select count(*) totalCnt
        from board 
    """
    row = db.executeOne(sql)
    totalCnt = int(row["totalCnt"])
    if 'pageNum' in request.values.keys():
        pageNum=int(request.values["pageNum"])
    else:
        pageNum=1 
    pager = CommonUtil.getPaging(pageNum, totalCnt)

    sql = """
         select id, title, writer, 
            date_format(wdate, '%%Y-%%m-%%d') wdate, hit, rnum
        from 
        (   
            select id, title, writer, wdate, hit,
            @rownum:=@rownum=1 as rnum
            from board, (select @rownum:=0) B 
            order by id desc
        ) A
        limit %s, 10       
    """
    rows = db.executeAll(sql, (int(pageNum-1)*10))    
    pager["rowList"]=rows
    db.close()
    return render_template("board/board_list.html", data=pager)

@bp.route('/write', methods=['GET', 'POST'])
def write():
    return render_template("board/board_write.html")


@bp.route('/save', methods=['POST'])
def save():
    file = request.files['upload']
    filename1=""
    if file : #파일 전송이 있을때 
        filename1 = CommonUtil.getFilename(file.filename)
        sfilename = os.path.join(current_app.config["UPLOAD_FOLDER"], 
                         filename1)
        file.save(sfilename)

    title = request.form['title']
    writer = request.form['writer']
    contents = request.form['contents']
    sql = """
    insert into board(title, writer, contents, wdate, hit, filename1)
    values
    (%s, %s, %s, now(), 0, %s)
    """
    db = Database()
    db.execute(sql, (title, writer, contents, filename1))
    db.close()
    return redirect("/board/list")



@bp.route('/view/<id>', methods=['GET', 'POST'])
def view(id):
    sql = """
        update board set hit=hit+1 where id=%s
    """
    db = Database()
    db.execute(sql, (id))

    sql = """
         select id, title, writer, 
        date_format(wdate, '%%Y-%%m-%%d') wdate, hit, contents, filename1
        from board 
        where id = %s
    """
    row = db.executeOne(sql, (id))
    db.close()
    return render_template("board/board_view.html", row=row)

from flask import send_from_directory
@bp.route('/download/<filename>')
def download(filename):
    uploads = current_app.config['UPLOAD_FOLDER']
    return send_from_directory(directory=uploads, path=filename)
