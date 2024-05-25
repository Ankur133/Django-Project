from django.shortcuts import render
import mysql.connector as sql
em=''
pas=''
# Create your views here.
def loginaction(request):
    global em,pas
    if request.method=="POST":
        m=sql.connect(host="localhost",user="root",passwd="1234",database='database2')
        cursor=m.cursor()
        d=request.POST
        for key,value in d.items():
            if key=="email":
                em=value
            if key=="password":
                pas=value

        c="select * from table2 where email='{}' and password='{}'".format(em,pas)
        cursor.execute(c)
        t=tuple(cursor.fetchall())
        if t==():
            return render(request,"error.html")
        else:
            return render(request,"welcome.html")


    return render(request,'login_page.html')
