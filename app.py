from flask import Flask,flash,redirect,render_template,url_for,request,jsonify,session,send_file,abort,flash
from flask_mysqldb import MySQL
from io import BytesIO
from otp import genotp
from sdmail import sendmail
from tokenreset import token
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

app=Flask(__name__)
app.secret_key='A@Bullela@_3'
app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD']='admin'
app.config['MYSQL_DB']='office'
app.config["SESSION_TYPE"] = "filesystem"
mysql=MySQL(app)
@app.route('/')
def home():
    return render_template('title.html')
@app.route('/signup.html')
def login():
    return render_template('signup.html')
@app.route('/adminlogin',methods=['GET','POST'])
def admin():
    if request.method=="POST":
        user=int(request.form['adminid'])
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT adminid from admin')
        users=cursor.fetchall()            
        password=request.form['password']
        cursor.execute('select password from admin where adminid=%s',[user])
        data=cursor.fetchone()
        cursor.close()
        if (user,) in users:
            if password==data[0]:
                session['admin']=user
                return redirect(url_for('adminpanel',adminid=user))
            else:
                flash('Invalid Password')
                return render_template('adminlogin.html')
        else:
            flash('Invalid user id')
            return render_template('adminlogin.html')      
    return render_template('adminlogin.html')

@app.route('/userlogin',methods=['GET','POST'])
def aspirentlogin():
    if session.get('aspirent'):
        return redirect(url_for('userhome',aspirent_id=session['user']))
    if request.method=="POST":
        user=int(request.form['username'])
        cursor=mysql.connection.cursor()
        cursor.execute('SELECT aspirentid from aspirent')
        users=cursor.fetchall()
        password=request.form['password']
        cursor.execute('select password from aspirent where aspirentid=%s',[user])
        data=cursor.fetchone()
        cursor.close()
        if (user,) in users:
            if password==data[0]:
                session["user"] =user
                return redirect(url_for('userhome',aspirent_id=user))
            else:
                flash('Invalid Password')
                return render_template('login.html')
        else:
            flash('Invalid id')
            return render_template('login.html')
    return render_template('login.html')
@app.route('/signup',methods=['GET','POST'])
def signup():
    if request.method=="POST":
        print(request.form)
        cursor=mysql.connection.cursor()
        id1=request.form['Id']
        cursor.execute('SELECT aspirentid from aspirent')
        data=cursor.fetchall()
        cursor.close()
        if (int(id1),) in data:
            flash('user Id already exists')
            return render_template('signup.html')
        Name=request.form['name']
        Age=request.form['Age']
        Experience=request.form['Experience']
        Company=request.form['Company']
        Email_id=request.form['Email Id']
        Phone_no=request.form['Phone']
       
        Gender=request.form['Gender']
        Password=request.form['Password']
        otp=genotp()
        subject='Thanks for registering'
        body = 'your one time password is- '+otp
        sendmail(Email_id,subject,body)
        return render_template('otp.html',otp=otp,id1=id1,Name=Name,Age=Age,Experience=Experience,Company=Company,Email_id=Email_id,Phone_no=Phone_no,Gender=Gender,Password=Password)
        '''cursor=mysql.connection.cursor()
        cursor.execute('insert into aspirent values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',[id1,name,Age,Experience,Company,Email_id,Phone_no,Gender,Password])
        mysql.connection.commit()
        cursor.close()
        flash('Signup successful')
        return render_template('signup.html')'''
    return render_template('signup.html')

@app.route('/otp/<otp>/<id1>/<Name>/<Age>/<Experience>/<Company>/<Email_id>/<Phone_no>/<Gender>/<Password>/',methods=['POST','GET'])
def getotp(otp,id1,Name,Age,Experience,Company,Email_id,Phone_no,Gender,Password):
    if request.method == 'POST':
        OTP=request.form['otp']
        if otp == OTP:
            cursor=mysql.connection.cursor()
            cursor.execute('insert into aspirent values(%s,%s,%s,%s,%s,%s,%s,%s,%s)',[id1,Name,Age,Experience,Company,Email_id,Phone_no,Gender,Password])
            mysql.connection.commit()
            cursor.close()
            flash('Details registered successfully')
            return redirect(url_for('aspirentlogin'))
        else:
            flash('wrong OTP')

    return render_template('otp.html',otp=otp,id1=id1,Name=Name,Age=Age,Experience=Experience,Company=Company,Email_id=Email_id,Phone_no=Phone_no,Gender=Gender,Password=Password)


@app.route('/forgotpassword',methods=('GET', 'POST'))
def forgotpassword():
    if request.method=='POST':
        id1 = request.form['id']
        cursor=mysql.connection.cursor()
        cursor.execute('select aspirentid from aspirent')
        deta=cursor.fetchall()
        if (int(id1),) in deta:
            cursor.execute('select emailid from aspirent where aspirentid=%s',[id1])
            data=cursor.fetchone()[0]
            cursor.close()
            subject=f'Reset Password for {data}'
            body=f'Reset the passwword using-\{request.host+url_for("resetpwd",token=token(id1,300))}'
            sendmail(data,subject,body)
            flash('Reset link sent to your registered mail id')
            return redirect(url_for('aspirentlogin'))
        else:
            flash('user does not exits')
    return render_template('forgot.html')

@app.route('/resetpwd/<token>',methods=('GET', 'POST'))
def resetpwd(token):
    try:
        s=Serializer(app.config['SECRET_KEY'])
        id1=s.loads(token)['user']
        if request.method=='POST':
            npwd = request.form['npassword']
            cpwd = request.form['cpassword']
            if npwd == cpwd:
                cursor=mysql.connection.cursor()
                cursor.execute('update aspirent set password=%s where aspirentid=%s',[npwd,id1])
                mysql.connection.commit()
                cursor.close()
                return 'Password reset Successfull'
            else:
                return 'Password does not matched try again'
        return render_template('newpassword.html')
    except Exception as e:
        abort(410,description='reset link expired')

@app.route('/adminsignup',methods=['GET','POST'])
def adminsignup():
    if request.method=="POST":
        cursor=mysql.connection.cursor()
        id1=request.form['Admin Id']
        cursor.execute('SELECT adminid from admin')
        data=cursor.fetchall()
        cursor.close()
        if (int(id1),) in data:
            flash('user Id already exists')
            return render_template('adminsignup.html')
        Name=request.form['Name']
        Gender=request.form['Gender']
        Email_id=request.form['Email Id']
        Password=request.form['Password']
        cursor=mysql.connection.cursor()
        cursor.execute('insert into admin values(%s,%s,%s,%s,%s)',[id1,Name,Gender,Email_id,Password])
        mysql.connection.commit()
        cursor.close()
        flash('Signup successful')
        return render_template('adminsignup.html')
    return render_template('adminsignup.html')


@app.route('/adminforgotpassword',methods=('GET', 'POST'))
def adminforgotpassword():
    if request.method=='POST':
        id1 = request.form['id']
        cursor=mysql.connection.cursor()
        cursor.execute('select adminid from admin')
        deta=cursor.fetchall()
        if (int(id1),) in deta:
            cursor.execute('select emailid from admin where adminid=%s',[id1])
            data=cursor.fetchone()[0]
            cursor.close()
            subject=f'Reset Password for {data}'
            body=f'Reset the passwword using-\{request.host+url_for("resetpwd",token=token(id1,300))}'
            sendmail(data,subject,body)
            flash('Reset link sent to your registered mail id')
            return redirect(url_for('login'))
        else:
            flash('user does not exits')
    return render_template('forgot.html')

@app.route('/adminresetpwd/<token>',methods=('GET', 'POST'))
def adminresetpwd(token):
    try:
        s=Serializer(app.config['SECRET_KEY'])
        id1=s.loads(token)['user']
        if request.method=='POST':
            npwd = request.form['npassword']
            cpwd = request.form['cpassword']
            if npwd == cpwd:
                cursor=mysql.connection.cursor()
                cursor.execute('update admin set password=%s where adminid=%s',[npwd,id1])
                mysql.connection.commit()
                cursor.close()
                return 'Password reset Successfull'
            else:
                return 'Password does not matched try again'
        return render_template('newpassword.html')
    except Exception as e:
        abort(410,description='reset link expired')

@app.route('/userhome/<aspirent_id>')
def userhome(aspirent_id):
    return render_template('userpanel.html')                
@app.route('/adminpanel/<adminid>')
def adminpanel(adminid):
    if session.get('admin'):
        return render_template('adminpanel.html')
    return redirect(url_for('admin'))
@app.route('/addnotifications',methods=['GET','POST'])
def add():
    if session.get('admin'):
        if request.method=='POST':
            id1=request.form['Notifid']
            File=request.files['File']
            filename=File.filename
            Notifname=request.form['Notifname']
            From_date=request.form['From']
            To_date=request.form['To']
            cursor=mysql.connection.cursor()
            cursor.execute('insert into notifications values(%s,%s,%s,%s,%s,%s,%s)',[id1,session.get('admin'),File.read(),Notifname,From_date,To_date,filename])
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('adminpanel',adminid=session['admin']))
        return render_template('add.html')
    return redirect(url_for('admin'))
@app.route('/editnotification',methods=['GET','POST'])
def edit():
    cursor=mysql.connection.cursor()
    cursor.execute('select notifid from notifications')
    data=cursor.fetchall()
    if session.get('admin'):
        if request.method=='POST':
            id1=request.form['choice']
            name=request.form['name']
            File=request.files['File']
            filename=File.filename
            From_date=request.form['From']
            To_date=request.form['To']
            cursor=mysql.connection.cursor()
            cursor.execute('update notifications set Fileupload=%s,notifname=%s,From_date=%s,To_date=%s,filename=%s where notifid=%s',[File.read(),name,From_date,To_date,filename,id1])
            mysql.connection.commit()
            cursor.close()
            return redirect(url_for('adminpanel',adminid=session['admin']))
        return render_template('edit.html',data=data)
    return redirect(url_for('admin'))
@app.route('/allnotification')
def allnotifications():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT Notifid,notifname,from_date,to_date from notifications')
    notifications=cursor.fetchall()
    cursor.close()
    return render_template('allnotifications.html',notifications=notifications)
@app.route('/viewfileadmin/<id1>')
def view(id1):
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT fileupload from notifications where notifid=%s',[id1])
    data=cursor.fetchone()[0]
    cursor.execute('select filename from notifications where notifid=%s',[id1])
    filename=cursor.fetchone()[0]
    #mention as_attachment=True to download the file--remove it to display the file
    return send_file(BytesIO(data),download_name=filename)
@app.route('/apply',methods=['GET','POST'])
def apply():
    if session.get('user'):
        cursor=mysql.connection.cursor()
        cursor.execute('select notifid from notifications')
        data=cursor.fetchall()
        if request.method=='POST':
            user=session.get('user')
            notifid=request.form['choice']
            File=request.files['File']
            filename=File.filename
            cursor=mysql.connection.cursor()
            cursor.execute('insert ignore into applicants(aspirentid,notifid,filename,fileupload) values(%s,%s,%s,%s)',[user,notifid,filename,File.read()])
            mysql.connection.commit()
            cursor.close()
        return render_template('apply.html',data=data)
    return redirect(url_for('userlogin'))
@app.route('/view-delete')
def dview():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT Notifid,notifname,from_date,to_date from notifications')
    notifications=cursor.fetchall()
    cursor.close()
    return render_template('delete.html',notifications=notifications)
@app.route('/delete/<id1>')
def delete(id1):
    cursor=mysql.connection.cursor()
    cursor.execute('delete from notifications where Notifid=%s',[id1])
    mysql.connection.commit()
    return redirect(url_for('dview'))
@app.route('/status')
def status():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT aspirentid,notifid,filename,applied_date,status from applicants')
    applicants=cursor.fetchall()
    return render_template('status.html',applicants=applicants)
@app.route('/viewfilestats/<id1>')
def view31(id1):
    print(type(id1))
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT fileupload from applicants where filename=%s',(id1,))
    data=cursor.fetchone()[0]
    return send_file(BytesIO(data),download_name=id1)
@app.route('/applicants')
def applicants():
    cursor=mysql.connection.cursor()
    cursor.execute('SELECT aspirentid,notifid,filename,applied_date,status from applicants')
    applicants=cursor.fetchall()
    return render_template('applicants.html',applicants=applicants)
@app.route('/update/<aspid>/<notid>',methods=['GET','POST'])
def update(aspid,notid):
    if request.method=='POST':
        print(request.form)
        update_status=request.form['updatestatus']
        cursor=mysql.connection.cursor()
        cursor.execute('UPDATE applicants set status=%s where aspirentid=%s and notifid=%s',[update_status,aspid,notid])
        mysql.connection.commit()
        return redirect(url_for('applicants'))
    return render_template('update.html')        
app.run(debug='True')
