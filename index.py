from flask import Flask,render_template, request
import pymysql
app=Flask(__name__)

@app.route("/",methods=["GET","POST"])
def  add_user():
    if request.method=='GET':
        return render_template("增加.html")
    username=request.form.get("user")
    password=request.form.get("pwd")
    mobile=request.form.get('mobile')

    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='330327',charset='utf8',db='data')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) 
    
    sql="insert into admin(username,password,mobile) value(%s,%s,%s) "
    cursor.execute(sql,[username,password,mobile])
    conn.commit()
    
    cursor.close()
    conn.close()
    
    return '添加成功'
@app.route("/show")
def show_user():
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='330327',charset='utf8',db='data')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) 
    
    sql="select * from admin"
    cursor.execute(sql)
    data_list=cursor.fetchall()
    
    
    cursor.close()
    conn.close()
    
    return render_template('查看.html',data_list=data_list)
@app.route('/delete',methods=["GET","POST"])
def delete_user():
    if request.method=='GET':
        return render_template("删除.html")
    username=request.form.get("user")
    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='330327',charset='utf8',db='data')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) 
    sql="delete from admin where username=%s"
    cursor.execute(sql,username)
    conn.commit()
    cursor.close()
    conn.close()
    
    return "删除成功"
@app.route('/remove',methods=["GET","POST"])
def remove_user():
    if request.method=='GET':
        return render_template("修改.html")
    username=request.form.get("user")
    password=request.form.get("pwd")
    mobile=request.form.get('mobile')

    conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='330327',charset='utf8',db='data')
    cursor=conn.cursor(cursor=pymysql.cursors.DictCursor) 
    sql="update admin set password=%s where username=%s"
    cursor.execute(sql,[password,username])
    sql="update admin set mobile=%s where username=%s"
    cursor.execute(sql,[mobile,username])
    conn.commit()
    cursor.close()
    conn.close()
    
    return "修改成功"
    
if __name__=='__main__':
    app.run()
