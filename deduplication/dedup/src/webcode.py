import base64
import hashlib
import os
import random
import string
import requests
from src.AESCLASS import encrypt, decrypt
from werkzeug.utils import secure_filename

from src.db import *
from flask import *

app = Flask(__name__)
app.secret_key="12345"
app.config['path']=str(os.path.dirname(os.path.abspath(__file__)))+"\static\\files"
app.config['path1']=str(os.path.dirname(os.path.abspath(__file__)))+"\static\\download"

@app.route('/')
def login():
    return  render_template("login_index.html")

@app.route('/add_teamleader',methods=['get','post'])
def add_teamleader():
    return render_template("admin/Add Team Leader.html")

@app.route('/team_leader',methods=['get','post'])
def team_leader():
    qry="SELECT * FROM `team leader`"
    res=selectall(qry)

    return render_template("admin/view_teamleader.html",val=res)



@app.route('/teamleader_reg',methods=['get','post'])
def teamleader_reg():
    fname=request.form['fname']
    lname = request.form['lname']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    username = request.form['username']
    password=request.form['password']

    qry="insert into login values(null,%s,%s,'team leader')"
    val=(username,password)
    id=iud(qry,val)
    qry="insert into `team leader` values(null,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(str(id),fname,lname,place,post,pin,phone,email)
    iud(qry,val)
    return ''' <script>alert("Team Leader added");window.location="/team_leader#about"</script>'''

@app.route('/delete_tleader',methods=['get','post'])
def delete_tleader():
    id=request.args.get('id')
    qry= "Delete from `team leader` where tid=%s"
    iud(qry,id)
    return ''' <script>alert("deleted successfully");window.location="/team_leader#about"</script>'''






@app.route('/add_work',methods=['get','post'])
def add_work():
    qry="SELECT * FROM `team leader`"
    res=selectall(qry)
    return render_template("admin/Add Work.html",val=res)

@app.route('/view_work',methods=['get','post'])
def view_work():
    qry = "SELECT work.*,`team leader`.`fname`,`lname` FROM `team leader` JOIN `work` ON `work`.`lid`=`team leader`.`lid`"
    res = selectall(qry)

    return render_template("admin/View Work.html", val=res)

@app.route('/delete_work',methods=['get','post'])
def delete_work():
    id=request.args.get('id')
    qry= 'Delete from work where wid=%s'
    iud(qry,id)
    return ''' <script>alert("work deleted");window.location="/view_work#about"</script>'''


@app.route('/work_reg',methods=['get','post'])
def work_reg():
    wname=request.form['work_name']
    tm=request.form['select']
    description = request.form['work_desc']
    complete_date = request.form['complete_date']
    qry="insert into work values(null,%s,%s,%s,%s,'pending')"
    val=(tm,wname,description,complete_date)
    iud(qry,val)
    return ''' <script>alert("work added");window.location="/view_work#about"</script>'''

@app.route('/add_member', methods=['get','post'])
def add_member():
    fname = request.form['fname']
    lname = request.form['lname']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    qry = "insert into login values(null,%s,%s,'member')"
    val = (username, password)
    id = iud(qry, val)
    qry = "insert into `member` values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val = (str(id),session['lid'] ,fname, lname, place, post, pin, phone, email)
    iud(qry, val)
    return ''' <script>alert("New Member added");window.location="/view_member"</script>'''


@app.route('/admin',methods=['get','post'])
def admin():
    q="SELECT * FROM `complaint` WHERE `reply`='pending'"
    r=selectall(q)
    if len(r)==0:
        session['c']=""
    else:
        session['c']="("+str(len(r))+")"
    return render_template("admin/admin_index.html")

@app.route('/complaint_reply',methods=['get','post'])
def complaint_reply():
    id=request.args.get('id')
    session['cid']=id
    return render_template("admin/compl_reply.html")

@app.route('/complaint_replysnd',methods=['get','post'])
def complaint_replysnd():
    reply=request.form['textfield']
    qry="update complaint set reply=%s where cid=%s"
    val=(reply,session['cid'])
    iud(qry,val)

    q = "SELECT * FROM `complaint` WHERE `reply`='pending'"
    r = selectall(q)
    if len(r) == 0:
        session['c'] = ""
    else:
        session['c'] = "("+str(len(r))+")"
    return '''<script>alert("success");window.location="/complaint#about"</script>'''

@app.route('/edit_team_leader',methods=['get','post'])
def edit_team_leader():
    tid=request.args.get('id')
    session['tid']=tid
    qry="select * from `team leader` where tid=%s "
    res=selectone(qry,tid)
    return render_template("admin/edit_teamleader.html",val=res)


@app.route('/edit_team_leader1',methods=['get','post'])
def edit_team_leader1():
    fname = request.form['fname']
    lname = request.form['lname']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    qry="UPDATE `team leader` SET `fname`=%s,`lname`=%s,`place`=%s,`post`=%s,`pin`=%s,`phone`=%s,`email`=%s WHERE `tid`=%s"
    val = ( fname, lname, place, post, pin, phone, email,session['tid'])
    iud(qry, val)
    return ''' <script>alert(" Team Leader edited");window.location="/team_leader#about"</script>'''









#<=================TeamLeader=======================

@app.route('/teamleader',methods=['get','post'])
def teamleader():
    qry = "SELECT * FROM `doubts` JOIN `member` ON `member`.`lid`=`doubts`.`mid` where `member`.`tid`=%s and doubts.reply='pending'"
    res = selectall2(qry, session['lid'])
    if len(res)==0:
        session['d']=""
    else:
        session['d']="("+str(len(res))+")"
    qr = "select * from `team leader` where lid=%s"
    val = selectone(qr, session['lid'])
    session['tlname']=val['fname']+" "+val['lname']
    return render_template("teamleader/team_leader.html")

@app.route('/member_reg', methods=['post'])
def member_reg():
    return render_template("teamleader/Add Member.html")


@app.route('/view_member',methods=['get','post'])
def view_member():
    qry="SELECT * FROM `member` where `tid`=%s"

    res=selectall2(qry,session['lid'])

    return render_template("teamleader/view_member.html",val=res)

@app.route('/delete_member',methods=['get','post'])
def delete_member():
    id=request.args.get('id')
    qry= 'Delete from member where mid=%s'
    iud(qry,id)
    return ''' <script>alert("member deleted successfully");window.location="/view_member"</script>'''

@app.route('/edit_member',methods=['get','post'])
def edit_member():
    mid=request.args.get('id')
    session['mid']=mid
    qry="select * from `member` where mid=%s "
    res=selectone(qry,mid)
    return render_template("teamleader/edit_member.html",val=res)


@app.route('/edit_member1',methods=['get','post'])
def edit_member1():
    fname = request.form['fname']
    lname = request.form['lname']
    place = request.form['place']
    post = request.form['post']
    pin = request.form['pin']
    phone = request.form['phone']
    email = request.form['email']
    qry="UPDATE `member` SET `fname`=%s,`lname`=%s,`place`=%s,`post`=%s,`pin`=%s,`phone`=%s,`email`=%s WHERE `mid`=%s"
    val = ( fname, lname, place, post, pin, phone, email,session['mid'])
    iud(qry, val)
    return ''' <script>alert(" Member edited");window.location="/view_member#about"</script>'''


@app.route('/tlview_work', methods=['get','post'])
def tlview_work():
    qry="SELECT * FROM `work` WHERE `lid`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("teamleader/view_work.html",val=res)


@app.route('/assign_work', methods=['get','post'])
def assign_work():
    id=request.args.get('id')
    session['wid']=id
    qry="SELECT * FROM `member` WHERE `tid`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("teamleader/assign_work.html",val=res)

@app.route('/assign_work1', methods=['get','post'])
def assign_work1():
    member=request.form['select']
    qry1="select * from assign_work where wid=%s"
    res1=selectone(qry1,session['wid'])
    print(res1,"hhhhhhhhhhhh")
    if res1 is None:
        qry="INSERT INTO `assign_work` VALUES(NULL,%s,%s,'pending')"
        val=(member,session['wid'])
        iud(qry,val)
        return '''<script>alert("assigned");window.location='/teamleader'</script>'''
    else:
        return '''<script>alert(" already assigned");window.location='/teamleader'</script>'''



@app.route('/view_doubt',methods=['get','post'])
def view_doubt():
    qry = "SELECT * FROM `doubts` JOIN `member` ON `member`.`lid`=`doubts`.`mid` where `member`.`tid`=%s and doubts.reply='pending'"
    res=selectall2(qry,session['lid'])
    print(res)
    return render_template("teamleader/view_doubt.html",val=res)

@app.route('/reply_doubt',methods=['get','post'])
def reply_doubt():
    id=request.args.get('id')
    session['did']=id

    return render_template("teamleader/reply_doubt.html")

@app.route('/reply_doubt1',methods=['get','post'])
def reply_doubt1():
    reply=request.form['textarea']
    qry="update doubts set reply=%s where did=%s"
    val=(reply,session['did'])
    iud(qry,val)
    qry = "SELECT * FROM `doubts` JOIN `member` ON `member`.`lid`=`doubts`.`mid` where `member`.`tid`=%s and doubts.reply='pending'"
    res = selectall2(qry, session['lid'])
    if len(res) == 0:
        session['d'] = ""
    else:
        session['d'] = "(" + str(len(res)) + ")"
    return '''<script>alert("success");window.location="/view_doubt#about"</script>'''



@app.route('/notifications',methods=['get','post'])
def notifications():
    return render_template("teamleader/Notification.html")

@app.route('/add_notification',methods=['get','post'])
def add_notification():
    replymsg = request.form['textfield3']
    qry= "INSERT INTO `notification` VALUES(NULL,%s,%s,CURDATE())"
    val = (session['lid'],replymsg)
    iud(qry, val)
    return ''' <script>alert("Notification sent successfully");window.location="/teamleader"</script>'''



@app.route('/view_feedback',methods=['get','post'])
def view_feedback():
    qry = "SELECT * FROM `feedback` JOIN `member` ON `member`.`lid`=`feedback`.`mid`  WHERE member.tid=%s"
    res = selectall2(qry,session['lid'])
    return render_template("teamleader/view_feedback.html",val=res)


@app.route('/complaint',methods=['get','post'])
def complaint():
    qry="select * from `complaint` join `member` on `complaint`.`lid`=`member`.`lid`"
    res=selectall(qry)
    return render_template("admin/complaint.html",val=res)

@app.route('/logincode',methods=['get','post'])
def logincode():
    username=request.form['textfield']
    password=request.form['textfield2']
    qry="select * from login where username=%s and password=%s"
    val=(username,password)
    res=selectone(qry,val)
    if res is None:
            return '''<script>alert("invalid"); window.location ='/'</script>'''
    elif res['type']=='admin':
            session['lid']=res['lid']
            return '''<script>alert("welcome"); window.location = '/admin'</script>'''
    elif res['type']=='team leader':
            session['lid'] = res['lid']
            return '''<script>alert("welcome"); window.location = '/teamleader'</script>'''
    elif res['type']=='member':
            session['lid'] = res['lid']
            return '''<script>alert("welcome"); window.location = '/member_home'</script>'''
    else:
        return '''<script>alert("invalid"); window.location ='/'</script>'''
#=============================user=================================

@app.route('/member_home',methods=['get','post'])
def member_home():
    qr = "select * from member where lid=%s"
    res=selectone(qr,session['lid'])
    session['mname']=res['fname']+" "+res['lname']
    return render_template("member/member_home.html")

@app.route('/memview_work',methods=['get','post'])
def memview_work():
    qry = "SELECT `assign_work`.*,`work`.`work_name`, `work`.`wid` AS workid,`work`.`work description`,`work`.`completion date` FROM `work` JOIN `assign_work` ON `assign_work`.`wid`=`work`.`wid` JOIN `member` ON `member`.`mid`=`assign_work`.`mid` WHERE `member`.`lid`=%s"
    res = selectall2(qry, session['lid'])
    print(res,'uuuuuuuuuu')
    return render_template("member/view_work.html", val=res)

@app.route('/updateworkstatus_member',methods=['get','post'])
def updateworkstatus_member():
    id=request.args.get('id')
    session['workid']=id
    return render_template("member/work_status.html")

@app.route('/updateworkstatus_member1',methods=['get','post'])
def updateworkstatus_member1():
    status=request.form['select']
    qry="UPDATE `assign_work` SET `status`=%s WHERE `wid`=%s"
    val=(status,session['workid'])
    iud(qry, val)
    qry = "UPDATE `work` SET `status`=%s WHERE `wid`=%s"
    val = (status, session['workid'])
    iud(qry, val)


    return ''' <script>alert("status updated  successfully");window.location="/memview_work#about"</script>'''






@app.route('/add_complaint',methods=['get','post'])
def add_complaint():
    return render_template("member/add_complaint.html")

@app.route('/add_complaint1',methods=['get','post'])
def add_complaint1():
    comp_msg = request.form['textarea']
    qry = "INSERT INTO `complaint` VALUES(%s,NULL,%s,CURDATE(),'pending')"
    val = (session['lid'], comp_msg)
    iud(qry,val)
    return ''' <script>alert("Complaint sent successfully");window.location="/view_complaint#about"</script>'''

@app.route('/view_complaint',methods=['get','post'])
def view_complaint():
    qry="SELECT * FROM `complaint` WHERE lid=%s"
    res=selectall2(qry,session['lid'])

    return render_template("member/view_complaint.html",val=res)

@app.route('/memview_doubt',methods=['get','post'])
def memview_doubt():
    qry="SELECT * FROM `doubts` WHERE `mid`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("member/memview_doubt.html",val=res)

@app.route('/add_doubt',methods=['get','post'])
def add_doubt():
    return render_template("member/add_doubt.html")

@app.route('/add_doubt1',methods=['get','post'])
def add_doubt1():
    db=request.form['textarea']
    qry="INSERT INTO `doubts` VALUES(NULL,%s,CURDATE(),%s,'pending')"
    val=(session['lid'],db)
    iud(qry,val)
    return ''' <script>alert("Doubt asked successfully");window.location="/memview_doubt#about"</script>'''






@app.route('/add_feedback',methods=['get','post'])
def add_feedback():
    return render_template("member/add_feedback.html")

@app.route('/add_feedback1',methods=['get','post'])
def add_feedback1():
    db=request.form['textarea']
    qry="INSERT INTO `feedback` VALUES(NULL,%s,CURDATE(),%s)"
    val=(session['lid'],db)
    iud(qry,val)
    return ''' <script>alert("Feedback sent successfully");window.location="/member_home"</script>'''



@app.route('/view_notifications',methods=['get','post'])
def view_notifications():
    qry="SELECT `notification`.*,`member`.* FROM  `member` JOIN `notification`ON `member`.`tid`=`notification`.`tlid` WHERE `member`.`lid`=%s"
    res=selectall2(qry,session['lid'])
    return render_template("member/view_notifications.html",val=res)


@app.route('/file_upload',methods=['get','post'])
def file_upload():
    return render_template("member/file_upload.html")

@app.route('/view_file',methods=['get','post'])
def view_file():
    q="SELECT * FROM `file` WHERE `lid`=%s"
    res=selectall2(q,session['lid'])
    print(res)
    return render_template("member/view_file.html",data=res)



@app.route('/dltfile',methods=['get','post'])
def dltfile():
    id=request.args.get('id')
    q="DELETE FROM `file` WHERE `fid`=%s"
    iud(q,id)
    return '''<script>alert("deleted");window.location="/view_file#about"</script>'''



@app.route('/upload_file',methods=['post'])
def upload_file():
    print(request.files)
    subject=request.form['textarea']
    file=request.files['file']
    lid=session['lid']
    fname=secure_filename(file.filename)
    file.save(os.path.join('static/uploads',fname))





    with open(os.path.join('static/uploads',fname), "rb") as imageFile:
        stri = base64.b64encode(imageFile.read())

    data1=stri
    hashvalue = hashlib.sha512(data1).hexdigest()

    print("======hash value ", hashvalue)

    tag = hashlib.sha512(hashvalue.encode('ascii')).hexdigest()

    random1 = ''.join([random.choice(string.digits) for n in range(32)])
    print("key",random1)
    with open(os.path.join('static/uploads',fname), "rb") as imageFile:
        stri = base64.b64encode(imageFile.read()).decode('utf-8')
        enc1 = encrypt(stri, random1).decode('utf-8')

        fh = open(os.path.join('static/uploads',fname), "wb")
        fh.write(base64.b64decode(enc1))
        fh.close()


    ekey = int(hashvalue, 16) ^ int(random1)
    print(ekey)

    pdata = base64.b64encode(data1)
    print("---------------------" )


    url = "http://127.0.0.1:1234//upload1"

    datas = {'id': lid, 'tag': tag, 'key': ekey}

    payload = datas
    local_file_to_send = os.path.join('static/uploads',fname)
    files = {
        'json': (None, json.dumps(payload), 'application/json'),
        'files': (os.path.basename(local_file_to_send), open(local_file_to_send, 'rb'), 'application/octet-stream')
             }
    r = requests.post(url, files=files)
    print(r.text)


    qry = "INSERT INTO `file` (`filename`,`lid`,`description`,`hash`,`date`) VALUES (%s,%s,%s,%s,curdate())"

    val = (fname,str(lid),subject,hashvalue)
    iud(qry, val)
    return '''<script>alert("Uploaded");window.location='/view_file#about'</script>'''


#========================DOWNLOAD====================================



@app.route('/dwnld1')
def dwnld1():
    id = request.args.get('id')
    qry="select * from file where fid=%s"
    h=selectone(qry,id)
    tag = hashlib.sha512(h['hash'].encode('ascii')).hexdigest()
    url = "http://127.0.0.1:1234/download"
    print(url,"==============================")
    datas = {'tag': tag,}
    payload = datas
    files = {
        'json': (None, json.dumps(payload), 'application/json'),
    }
    r = requests.post(url, files=files)
    rr=r.text.split('"',8)
    print("-------------------------------------")
    print(rr)
    print(r,"**************&&&&&&&&&&")
    print(r.text)
    pth=rr[3]
    pth=pth.replace("\\\\","\\")
    print(pth,"+++++++++++++++++++++")
    print("-------------------------------------")
    url = "http://127.0.0.1:1234/key"
    datas = {'tag': tag, }
    payload = datas
    files = {
        'json': (None, json.dumps(payload), 'application/json'),
    }
    id = request.args.get('id')
    r1 = requests.post(url, files=files)
    print(r1.text, "qwertyuio")
    rr1 = r1.text.split('"', 8)
    print("-----------------",rr1)
    key = int(h['hash'], 16) ^ int(rr1[3])
    print(key)
    if (len(str(key)) != 32):
        key = "0" + str(key)
    print("hash=======",h['hash'])
    print("key=======",key)
    qry="SELECT `fid`,`filename`,`date` FROM `file` WHERE `fid`=%s"
    dataa = selectone(qry,id)
    print(dataa)
    try:
        with open(pth, "rb") as imageFile:

            stri = base64.b64encode(imageFile.read()).decode('utf-8')
            print("keyy",str(key),"*****************",stri,"=======")
            # dec2 = decrypt(stri, str(key))
            dec2 = decrypt(stri, str(key)).decode('utf-8')
            print(dec2,"=======================")
            print(os.path.join(app.config['path1'], dataa['filename']),"++++++++++++++++++++++++++++++++++++++")
            fh1 = open(os.path.join(app.config['path1'], dataa['filename']), "wb")
            fh1.write(base64.b64decode(dec2))
            fh1.close()
            print("final",dataa)
    except:
        try:
            with open(pth, "rb") as imageFile:
                stri = base64.b64encode(imageFile.read()).decode('utf-8')

                dec2 = decrypt(stri, key).decode('utf-8')

                fh1 = open(os.path.join(app.config['path1'], dataa['filename']), "wb")
                fh1.write(base64.b64decode(dec2))
                fh1.close()
        except:
            pass

    return render_template('member/download.html', val=dataa)

app.run(debug=True)