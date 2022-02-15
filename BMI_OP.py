from tkinter import *
from PIL import ImageTk, Image
import os
import mysql.connector as sql
import tkinter.ttk as ttk
dbcon=sql.connect(host="localhost",database="BMI",user="root",passwd="candy123")
dbcursor=dbcon.cursor()

def NXT_WIN():
    global root
    try:
        root.destroy()
    except:
        pass
    root = Tk()
    root.geometry("1380x730")
    root.title("BODY MASS INDEX CALCULATOR")

    img= ImageTk.PhotoImage(Image.open("BMI_background1.jpeg").resize((1380,768)))
    L1=Label(root,image=img)
    L1.place(x=-10,y=-10)

    heading=Label(root,text="DELHI PUBLIC SCHOOL VADODARA",bg="black",fg="white")
    heading.config(font=("Ariel",40))
    heading.place(x=230,y=5)

    sub_heading=Label(root,text="HEALTH DEPARTMENT",bg="black",fg="white")
    sub_heading.config(font=("Ariel",40))
    sub_heading.place(x=385,y=70)

    L2=Label(root,text="NAME:",bg="black",fg="white")
    L2.config(font=("Ariel",15))
    L2.place(x=100,y=230)

    E1=Entry(root,width=40)
    E1.place(x=180,y=235)
    

    L3=Label(root,text="CLASS:",bg="black",fg="white")
    L3.config(font=("Ariel",15))
    L3.place(x=100,y=260)

    E2=Entry(root,width=10)
    E2.place(x=180,y=265)
    
    L4=Label(root,text="SECTION:",bg="black",fg="white")
    L4.config(font=("Ariel",15))
    L4.place(x=250,y=260)

    E3=Entry(root,width=10)
    E3.place(x=350,y=265)
    
    L5=Label(root,text="GENDER(M/F):",bg="black",fg="white")
    L5.config(font=("Ariel",15))
    L5.place(x=100,y=290)

    E4=Entry(root,width=10)
    E4.place(x=250,y=295)
    
    L9=Label(root,text="AGE:",bg="black",fg="white")
    L9.config(font=("Ariel",15))
    L9.place(x=100,y=320)

    E5=Entry(root,width=10)
    E5.place(x=170,y=325)
    
    L6=Label(root,text="ANY OTHER SPECIFICATIONS:",bg="black",fg="white")
    L6.config(font=("Ariel",15))
    L6.place(x=490,y=290)

    E6=Entry(root,width=20)
    E6.place(x=790,y=290,width=200,height=100)
    
    L7=Label(root,text="WEIGHT(IN(KG)):",bg="black",fg="white")
    L7.config(font=("Ariel",15))
    L7.place(x=100,y=450)

    E7=Entry(root,width=10)
    E7.place(x=280,y=455)

    L8=Label(root,text="HEIGHT(IN(M)):",bg="black",fg="white")
    L8.config(font=("Ariel",15))
    L8.place(x=100,y=480)

    E8=Entry(root,width=10)
    E8.place(x=280,y=485)
    
    B1=Button(root,text="RETURN HOME",command=mainscreen)
    B1.place(x=15,y=20)

    B2=Button(root,text="CALCULATE BMI",command=lambda:BMI_MAIN("NO BMI CALCULATED"))
    B2.place(x=980,y=650)

    B3=Button(root,text="CLICK HERE TO CONFIRM YOUR DETAILS",command=lambda:CALCULATION(E1.get(),E4.get(),E5.get(),E6.get(),E7.get(),E8.get()))
    B3.place(x=100,y=550)
    root.mainloop()

def BMI_MAIN(BMI):
    global root
    root.destroy()

    root=Tk()
    root.geometry("1380x730")
    root.title("BODY MASS INDEX CALCULATOR")

    img= ImageTk.PhotoImage(Image.open("BMI_background1.jpeg").resize((1380,768)))
    L1=Label(root,image=img)
    L1.place(x=-10,y=-10)

    heading=Label(root,text="DELHI PUBLIC SCHOOL VADODARA",bg="black",fg="white")
    heading.config(font=("Ariel",40))
    heading.place(x=230,y=5)

    sub_heading=Label(root,text="HEALTH DEPARTMENT",bg="black",fg="white")
    sub_heading.config(font=("Ariel",40))
    sub_heading.place(x=385,y=70)

    L2=Label(root,text="YOUR BMI:",bg="black",fg="white")
    L2.config(font=("Ariel",30))
    L2.place(x=50,y=200)

    L10=Label(root,text=BMI,bg="black",fg="white")
    L10.config(font=("Ariel",30))
    L10.place(x=280,y=200)

    img1=ImageTk.PhotoImage(Image.open("TABLE.jpeg").resize((600,500)))
    L10=Label(root,image=img1)
    L10.place(x=700,y=150)
    

    B1=Button(root,text="RETURN HOME",command=mainscreen)
    B1.place(x=10,y=10)

    B2=Button(root,text="CHANGE YOUR DETAILS",command=NXT_WIN)
    B2.place(x=10,y=40)

    frm1 = Frame(root)
    scrollbarx=Scrollbar(frm1,orient = HORIZONTAL)
    scrollbary=Scrollbar(frm1,orient = VERTICAL)
    tree1 = ttk.Treeview(frm1,columns=("NAME","AGE","SEX","WEIGHT","HEIGHT","BMI","REMARKS"),selectmode="extended",yscrollcommand=scrollbary.set,xscrollcommand=scrollbarx.set)
    tree1["columns"] = ("1","2","3","4","5","6","7")
    tree1.heading("#1",text="NAME")
    tree1.heading("#2",text="AGE")
    tree1.heading("#3",text="GENDER")
    tree1.heading("#4",text="WEIGHT")
    tree1.heading("#5",text="HEIGHT")
    tree1.heading("#6",text="BMI")
    tree1.heading("#7",text="REMARKS")

    tree1.column("#0",minwidth=10,width=0)
    tree1.column("#1",minwidth=10,width=60)
    tree1.column("#2",minwidth=10,width=60)
    tree1.column("#3",minwidth=10,width=60)
    tree1.column("#4",minwidth=10,width=60)
    tree1.column("#5",minwidth=10,width=60)
    tree1.column("#6",minwidth=10,width=70)
    tree1.column("#7",minwidth=10,width=70)
    
    scrollbary.config(command=tree1.yview)
    scrollbarx.config(command=tree1.xview)
    scrollbary.pack(side = RIGHT,fill = Y)
    scrollbarx.pack(side = BOTTOM,fill = X)
    tree1.pack()
    frm1.place(x=100,y=450)

    sql1 = "select * from BMI_DB"
    dbcursor.execute(sql1)
    var1=dbcursor.fetchall()
    for record in var1:
        tree1.insert('','end',values=(record[0],record[1],record[2],record[3],record[4],record[5],record[6]))
    

    root.mainloop()

def CALCULATION(NAME,SEX,AGE,OTHERS,WEIGHT,HEIGHT):
    
    BMI=float(WEIGHT)/(float(HEIGHT)**2)
    
    sql1="INSERT INTO BMI_DB VALUES('{}',{},'{}',{},{},{},'{}')".format(NAME,AGE,SEX,WEIGHT,HEIGHT,BMI,OTHERS)
    dbcursor.execute(sql1)

    dbcon.commit()

    BMI_MAIN(BMI)

def mainscreen():
    global root
    try:
        root.destroy()
    except:
        pass

    root = Tk()
    root.geometry("1380x730")
    root.title("BODY MASS INDEX CALCULATOR")

    img= ImageTk.PhotoImage(Image.open("BMI_background1.jpeg").resize((1380,768)))
    L1=Label(root,image=img)
    L1.place(x=-10,y=-10)

    heading=Label(root,text="DELHI PUBLIC SCHOOL VADODARA",bg="black",fg="white")
    heading.config(font=("Ariel",40))
    heading.place(x=230,y=5)

    sub_heading=Label(root,text="HEALTH DEPARTMENT",bg="black",fg="white")
    sub_heading.config(font=("Ariel",40))
    sub_heading.place(x=385,y=70)

    main_heading=Label(root,text="STUDENT BMI CALCULATOR",bg="black",fg="white")
    main_heading.config(font=("Ariel",40))
    main_heading.place(x=315,y=210)

    B1=Button(root,text="PROCEED",command=NXT_WIN)
    B1.config(font=("Ariel",17),height=3,width=15)
    B1.place(x=1160,y=600)

    L2=Label(root,text="CREATED BY:-SKYZE",bg="black",fg="white")
    L2.config(font=("Ariel",7))
    L2.place(x=0,y=670)
    
    root.mainloop()

mainscreen()

    
    
    
