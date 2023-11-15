from tkinter import *
import sqlite3 as sq

def clear_window(main):
    for widget in main.winfo_children():
        widget.destroy()

def user(): #this open the registeration form for the user.

    clear_window(main)
    
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
        cur.execute("insert into data values (?,?,?,?,?)",(name,surname,gender,country,phone))
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
  

def admin(): #this will open the admin panel for the admin
    
    clear_window(main)

    main.geometry("600x500")
    main.title("Admin Panel")
    main.resizable(0,0)

    a1=StringVar()
    a2=StringVar()

    photo=PhotoImage(file = r"C:\Users\dayaa\Desktop\⠀\Jupyter-notebooks\Project\xzsvi4kn.png")
    L1=Label(image = photo)
    L1.pack()

    L2=Label(main,text="Log_id :",font=("Comic Sans MS",15),width=10)
    L2.place(x=90,y=93)
    E1=Entry(main,width=30,font=("Arail",12),textvariable=a1)
    E1.place(x=230,y=100)

    L3=Label(main,text="Password :",font=("Comic Sans MS",15),width=10)
    L3.place(x=90,y=133)
    E2=Entry(main,width=30,font=("Arail",12),textvariable=a2)
    E2.place(x=230,y=140)

    L4=Label(main,text="Admin Panel",fg="red",
    font=("Comic Sans MS",20,"underline"),width=20)
    L4.place(x=140,y=20)


    
    def login(): 
        global t
        log_id=a1.get()
        password=a2.get()
        if (password==" ") and (log_id==" "):
            dataprinting()
        else:
            t=Text(main,width=28,height=1,font=("Comic Sans MS",15))
            t.place(x=125,y=400)
            t.insert("end","--Please Enter Correct Password--")

    def dataprinting():
        try:
            t.destroy()
        except NameError:
            pass
        L2.destroy()
        E1.destroy()
        L3.destroy()
        E2.destroy()
        b1.destroy()
        L4.destroy()

        Label(main,text="Candidates Name:",fg="black",font=("Comic Sans MS",13),width=15).place(x=20,y=20)

        conn=sq.connect("RegForm.db")
        cur=conn.cursor()

        try:
            cur.execute("select name from data")
            a=cur.fetchall()
        except sq.OperationalError:
            print("---No Candidates---")
            return False

        l=[]
        for i in a:
            l.append(i[0])
        value=StringVar()
        menu=OptionMenu(main,value,*l)
        menu.place(x=200,y=20)
        value.set("Select student")

        conn=sq.connect("RegForm.db")
        c=conn.cursor()

        def submit():
            selected_value=value.get()
            if selected_value == "Select student":
                return
            # if i don't put this "," after the selected_value it going to show the error.
            # sqlite3.ProgrammingError: Incorrect number of bindings supplied. 
            # The current statement uses 1, and there are 14 supplied.
            c.execute("select * from data where name = ? ",(selected_value,)) 
            candi_data=c.fetchall()
            final_textbox=Text(main,height=5,width=25,font=("Comic Sans MS",15))
            final_textbox.place(x=20,y=60)
            for i in candi_data:
                final_textbox.insert("end",f"Name: {i[0]}\n")
                final_textbox.insert("end",f"Surname: {i[1]}\n")
                final_textbox.insert("end",f"Gender: {i[2]}\n")
                final_textbox.insert("end",f"Country: {i[3]}\n")
                final_textbox.insert("end",f"Phone no: {i[4]}")
            
        submit_button = Button(main,text="Submit",fg="White",bg="red",font=("Comic Sans MS",15),command=submit)
        submit_button.place(x=380, y=20,height=40,width=120)


    b1=Button(main,text="Log In",fg="White",bg="red",font=("Comic Sans MS",15),command=login)
    b1.place(x=200,y=200,height=40,width=200)
    main.mainloop()
    


#main program
main=Tk()
main.geometry("600x500")
main.title("Registration Form")
main.resizable(0,0)

photo=PhotoImage(file = r"C:\Users\dayaa\Desktop\⠀\Jupyter-notebooks\Project\xzsvi4kn.png")
l1=Label(image = photo)
l1.pack()

Label(main,text="Registration Form",fg="red",font=("Comic Sans MS",20,"underline"),width=20).place(x=140,y=20)

b1=Button(main,text="User",fg="White",bg="red",font=("Comic Sans MS",15),command=user)
b1.place(x=100,y=150,height=40,width=120)

b2=Button(main,text="Admin",fg="White",bg="red",font=("Comic Sans MS",15),command=admin)
b2.place(x=380,y=150,height=40,width=120)

main.mainloop()
print("--Thank you for using this application--")



