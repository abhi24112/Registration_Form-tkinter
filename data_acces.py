import sqlite3 as sq
from tkinter import *

main=Tk()
main.geometry("600x550")
main.title("Admin Panel")
main.resizable(0,0)

a1=StringVar()
a2=StringVar()

photo=PhotoImage(file = r"C:\Users\dayaa\Desktop\⠀\Jupyter-notebooks\Project\xzsvi4kn.png")
l1=Label(image = photo)
l1.pack()

Label(main,text="Log_id :",font=("Comic Sans MS",15),width=10).place(x=90,y=93)
E1=Entry(main,width=30,font=("Arail",12),textvariable=a1).place(x=230,y=100)

Label(main,text="Password :",font=("Comic Sans MS",15),width=10).place(x=90,y=133)
E1=Entry(main,width=30,font=("Arail",12),textvariable=a2).place(x=230,y=140)

Label(main,text="Admin Panel",fg="red",
font=("Comic Sans MS",20,"underline"),width=20).place(x=140,y=20)


def login():
    log_id=a1.get()
    password=a2.get()
    if (password=="9910") and (log_id=="abhishek"):
        
        Label(main,text="Data :",font=("Comic Sans MS",15),width=10).place(x=25,y=250)
        t=Text(main,width=28,height=1,font=("Comic Sans MS",15))
        t.place(x=125,y=400)
        t.delete(1.0,END)
        
        def admin():
            conn=sq.connect("RegForm.db")
            cur=conn.cursor()
            try:
                cur.execute("select * from data")
            except sq.OperationalError:
                print("---No Candidates---")
                return False
            a=cur.fetchall()
            # t=Text(main,width=28,height=1,font=("Comic Sans MS",15))
            t = Text(main, width=30, height=10, font=("Comic Sans MS",15))
            t.place(x=125,y=250)
            count=1
            for i in a:
                # print("Name:",i[0],"\n")
                # print("Surname:",i[1])
                # print("Gender:",i[2])
                # print("Country:",i[3])
                # print("Phone no. :",i[4],"\n")
                data = f"\n{count} Person Data:\n Name: {i[0]}\nSurname: {i[1]}\nGender: {i[2]}\nCountry: {i[3]}\nPhone no: {i[4]}\n"
                t.insert("end", data)
                count+=1
            conn.close()
        admin()
        
    else:
        t=Text(main,width=28,height=1,font=("Comic Sans MS",15))
        t.place(x=125,y=400)
        t.insert("end","--Please Enter Correct Password--")

b1=Button(main,text="Log In",fg="White",bg="red",font=("Comic Sans MS",15),command=login)
b1.place(x=200,y=200,height=40,width=200)

# b1=Button(main,text="Log In",fg="White",bg="red",font=("Comic Sans MS",15),command=admin)
# b1.place(x=200,y=200,height=40,width=200)

main.mainloop()
print("===Thank you for using this application===")