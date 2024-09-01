
import  ast

import os

import pymysql
import requests
from flask import jsonify
from flask.app import Flask
from flask.globals import request
from flask.templating import render_template
from werkzeug.utils import secure_filename

root=Flask(__name__)

root.secret_key='sk'
root.config['path'] = str(os.path.dirname(os.path.abspath(__file__)))+"\static\File"
con=pymysql.connect(host='localhost', user='root', passwd='', port=3306, db='dedup1')
cmd=con.cursor()


@root.route('/upload1', methods=['GET','POST'])
def upload1():
    try:
        RequestValues=request.values
        print(RequestValues)


        RequestForm=request.form
        print(RequestForm)

        so=RequestForm
        json_of_metadatas=so.to_dict(flat=False)
        print(json_of_metadatas)


        MetdatasFromJSONO=json_of_metadatas['json']
        print(MetdatasFromJSONO)


        MetdatasFromJSONO=MetdatasFromJSONO[0]
        print(MetdatasFromJSONO)


        strMetadatasFroJSONO= str(MetdatasFromJSONO)
        MetdatasDICT=ast.literal_eval(strMetadatasFroJSONO)
        print(MetdatasDICT)


        cmd.execute("select * from filetable where tag='"+str(MetdatasDICT["tag"])+"'")
        s=cmd.fetchone()
        print(str(MetdatasDICT["tag"]))
        print(s)
        f = request.files['files']
        print(str(MetdatasDICT["key"]))
        if s is None:

            cmd.execute("insert into filekey values(null,'"+str(secure_filename(f.filename))+"','"+str(MetdatasDICT["key"])+"')")
            id=con.insert_id()
            cmd.execute("insert into filetable values(null,'"+str(id)+"','"+str(MetdatasDICT["id"])+"','"+MetdatasDICT["tag"]+"',curdate())")
            con.commit()
            f.save(str(os.path.join(root.config['path'],secure_filename(f.filename))))

            print("FILE SAVED LOCALY")

        else:
            cmd.execute("insert into filetable values(null,'"+str(s[1])+"','"+str(MetdatasDICT["id"])+"','"+MetdatasDICT["tag"]+"',curdate())")
            con.commit()
        return jsonify(status="OK")
    except Exception as e:
        print(str(e))
        return jsonify(status="Error: "+str(e))
    return jsonify(status="missing")



@root.route('/download', methods=['GET','POST'])
def download():
    try:

        RequestValues=request.values

        RequestForm=request.form

        so=RequestForm
        json_of_metadatas=so.to_dict(flat=False)

        MetdatasFromJSONO=json_of_metadatas['json']

        MetdatasFromJSONO=MetdatasFromJSONO[0]
        strMetadatasFroJSONO= str(MetdatasFromJSONO)
        MetdatasDICT=ast.literal_eval(strMetadatasFroJSONO)
        cmd.execute("select * from filetable where tag='" + str(MetdatasDICT["tag"]) + "'")
        s = cmd.fetchone()
        print(s,"===========================")
        if s is None:
            return jsonify(status="missing")
        else:
            print('haiiiiii')
            cmd.execute("select gid,fname from filekey where gid='"+str(s[1])+"'")
            x=cmd.fetchone()
            print(x)

            print(str(os.path.join(root.config['path'],str(x[1]))))
            pth=str(os.path.join(root.config['path'],str(x[1])))
            return jsonify(status= pth)
    except Exception as e:
        print(str(e))
        return jsonify(status="Error: "+str(e))
    return jsonify(status="missing")

@root.route('/key', methods=['GET','POST'])
def key():
    try:
        RequestValues = request.values
        print(RequestValues)
        RequestForm = request.form
        print(RequestForm)
        so = RequestForm
        json_of_metadatas = so.to_dict(flat=False)
        print(json_of_metadatas)
        MetdatasFromJSONO = json_of_metadatas['json']
        print(MetdatasFromJSONO)

        MetdatasFromJSONO = MetdatasFromJSONO[0]
        print(MetdatasFromJSONO)

        strMetadatasFroJSONO = str(MetdatasFromJSONO)
        MetdatasDICT = ast.literal_eval(strMetadatasFroJSONO)
        print(MetdatasDICT)

        cmd.execute("select * from filetable where tag='" + str(MetdatasDICT["tag"]) + "'")
        k = cmd.fetchone()
        if k is None:
            return jsonify(status="missing")
        else:
            cmd.execute("select * from filekey where gid='"+str(k[1])+"'")
            m=cmd.fetchone()
            return jsonify(status= str(m[2]) )

    except Exception as e:
        print(str(e))
        return jsonify(status="Error: " + str(e))
    return jsonify(status="missing")

@root.route('/verkey', methods=['GET','POST'])
def verkey():
    try:


        RequestValues = request.values


        RequestForm = request.form


        so = RequestForm
        json_of_metadatas = so.to_dict(flat=False)


        MetdatasFromJSONO = json_of_metadatas['json']


        MetdatasFromJSONO = MetdatasFromJSONO[0]


        strMetadatasFroJSONO = str(MetdatasFromJSONO)
        MetdatasDICT = ast.literal_eval(strMetadatasFroJSONO)

        uid=str(MetdatasDICT["uid"])
        cmd.execute("select gid from filetable where tag='" + str(MetdatasDICT["tag"]) + "'")
        dt = cmd.fetchone()

        gid=str(dt[0])
        print(gid)

        k=""
        cmd.execute("select distinct uid from filetable where gid='"+str(dt[0])+"' order by uid")
        z = cmd.fetchall()
        print("1111=====",z)
        for i in z:
            k=k+str(i[0])+","
        k=k[:len(k)-1]
        cmd.execute("SELECT   id FROM            tree WHERE        (lc LIKE 'u%') AND (rc IN (" + k + ")) order by id")
        g=cmd.fetchall()

        print("2==",g)
        gk=""
        gk1=[]
        for gg in g:
            gk1.append(gg[0])
        gkl1=[]
        print(gk1)
        for i in gk1:
            id=i
            f=True
            while f:
                print(gk1,"gk1")
                cmd.execute("select p from tree where id='"+str(id)+"'")
                p=cmd.fetchone()
                print("333======",p)
                cmd.execute("select * from tree where id='"+str(p[0])+"'")
                dtt=cmd.fetchall()
                print("4====",dtt)
                gklc=[]

                for j in dtt:
                    gklc.append(j[2])
                    gklc.append(j[3])
                for j in  gklc:
                    print(gk1,"gk1")
                    print(j,"j")
                    if(gk1.__contains__(j)):
                        print("noooo", j)
                        f = True
                        gkl1.append(id)

                    else:

                        print("okkkkk", j)
                        f = False
                if(f==True):
                    id=int(p[0])


        gklist=[]
        for i in range (len(gk1)):
            if(gklist.__contains__(gk1[i])):
                f = True
            else:
                f = False
                gklist.append(gk1[i])
                gk=gk+str(gk1[i])+"#"
        gk = gk[:len(gk) - 1]
        cmd.execute("select * from  tree where lc='u' '" + str(MetdatasDICT["uid"])+"'")
        dt=cmd.fetchall()
        print("555===",dt)


        pk=""

        if(len(dt)>0):
            pk=pk+str(dt[0][0])


        while(str(dt[0][1]) !="0" ):
            cmd.execute("select * from tree where id='"+str(dt[0][1])+"'")
            dt=cmd.fetchall()
            pk=pk+"#"+str(dt[0][0])
            print("666====",dt)
        ka=gk.split('#')
        pka=pk.split('#')

        print(gk + " gk")
        print(pk + " pk")

        keky=""
        for i in range (0,len(ka)):
            for j in range (0,len(pka)):
                if (ka[i]==pka[j]):
                    keky=ka[i]

                    break
        print(keky)
        cmd.execute("select key_s from key_ss where id='"+keky+"' ")
        s=cmd.fetchall()
        print("77777===",s)
        keky=str(s[0][0])
        print("keyyyyy--------",keky)
        return jsonify(status="OK: " + keky)



    except Exception as e:
        print(str(e))
        return jsonify(status="Fail: "+str(e))

























if(__name__=="__main__"):
    root.run(port=1234)

