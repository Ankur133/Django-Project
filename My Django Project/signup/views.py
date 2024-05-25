from django.shortcuts import render
import mysql.connector as sql
fn=''
ln=''
s=''
em=''
pas=''
# Create your views here.
def signupaction(request):
    global fn,ln,s,em,pas
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='database2')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="first_name":
                fn=value
            if key=="last_name":
                ln=value
            if key=="sex":
                s=value
            if key=="email":
                em=value
            if key=="password":
                pas=value

        c="insert into table2 Values('{}','{}','{}','{}','{}')".format(fn,ln,s,em,pas)
        cursor.execute(c)
        m.commit()

    return render(request,'signup_page.html')
