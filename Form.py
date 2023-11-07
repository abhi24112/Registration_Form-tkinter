from tkinter import *
import sqlite3 as sq
    
main=Tk()
main.geometry("600x500")
main.title("Registration Form")
main.resizable(0,0)

v1=StringVar()
v2=StringVar()
gen=StringVar()
c=StringVar()
p=StringVar()

photo=PhotoImage(file = r"C:\Users\dayaa\Desktop\⠀\Jupyter-notebooks\Project\xzsvi4kn.png")
l1=Label(image = photo)
l1.pack()

Label(main,text="Registration Form",fg="red",
    font=("Comic Sans MS",20,"underline"),width=20).place(x=140,y=20)

#Entry for Name and Surname
Label(main,text="Name :",font=("Comic Sans MS",15),width=10).place(x=90,y=93)
e1=Entry(main,width=30,font=("Arail",12),textvariable=v1).place(x=230,y=100)

Label(main,text="Surname :",font=("Comic Sans MS",15),width=10).place(x=90,y=133)
e2=Entry(main,width=30,font=("Arail",12),textvariable=v2).place(x=230,y=140)

#Gender
Label(main,text="Gender :",font=("Comic Sans MS",15),width=10).place(x=90,y=173)
Radiobutton(main,text="Female",font=("Arail",12),value="female",padx=5,variable=gen).place(x=230,y=180)
Radiobutton(main,text="Male",font=("Arail",12),value="male",padx=20,variable=gen).place(x=350,y=180)

#Country
Label(main,text="Country :",width=10,font=("Comic Sans MS",15)).place(x=90,y=213)
l=['India','Canda','America','Africa','Russia']
m1=OptionMenu(main,c,*l).place(x=230,y=213)
c.set("Select Country")

#phone number
Label(main,text="Phone no. :",width=10,font=("Comic Sans MS",15)).place(x=90,y=253)
e3=Entry(main,width=30,font=("Arail",12),textvariable=p).place(x=230,y=260)

#Cross Button
b1=Button(main,text="X",fg="red",command=main.destroy)
b1.place(x=550, y=0, width=50, height=30)



#database
def database():
    name=v1.get()
    surname=v2.get()
    gender=gen.get()
    country=c.get()
    phone=p.get()

    if not name or not surname or not gender or not country or not phone:
        t=Text(main,width=28,height=1,font=("Comic Sans MS",15))
        t.place(x=125,y=400)
        t.insert("end","--Please fill all the entry Correctly--")
        return 
    
    conn=sq.connect("RegForm.db")
    cur=conn.cursor()
    cur.execute("""create table if not exists data
              (Name text,Surname text,Gender text,Country text,Phone_no text)""")
    cur.execute("""insert into data values (?,?,?,?,?)""",(name,surname,gender,country,phone))
    conn.commit()
    cur.close()
    conn.close()
    #thank label
    t=Text(main,width=18,height=1,font=("Comic Sans MS",15))
    t.place(x=200,y=400)
    t.insert("end","You form is submitted")

#Submit button
b1=Button(main,text="Submit",fg="White",bg="red",font=("Comic Sans MS",15),command=database)
b1.place(x=250,y=300,height=40,width=120)

main.mainloop()
print("--Thank you for using this application--")