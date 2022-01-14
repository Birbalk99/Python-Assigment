import tkinter as tk
from tkinter import ttk
from tkinter import *
import os


def login():
    user=User_name.get()
    code=Password.get()
    #user="Birbal"
    #code="12345"

    if user=="Birbal" and code =="12345":
        root=tk.Tk()
        root.title("Value")
        root.geometry("500x300")
        root.configure(bg="#d7dae2")
        root.resizable(False,False)

#--------------------------------- main page ------------------------------------
        ttk.Label(root, text ="input1",font = ("Times New Roman",10)).grid(row =1,column=1)
        ttk.Label(root, text ="input2",font = ("Times New Roman",10)).grid(row =2,column=1)
        ttk.Label(root, text ="input3",font = ("Times New Roman",10)).grid(row =3,column=1)
        ttk.Label(root, text ="input4",font = ("Times New Roman",10)).grid(row =4,column=1)
        ttk.Label(root, text ="input5",font = ("Times New Roman",10)).grid(row =5,column=1)
        ttk.Label(root, text ="input6",font = ("Times New Roman",10)).grid(row =6,column=1)
        ttk.Label(root, text ="input7",font = ("Times New Roman",10)).grid(row =7,column=1)
        ttk.Label(root, text ="input8",font = ("Times New Roman",10)).grid(row =8,column=1)
        ttk.Label(root, text ="input9",font = ("Times New Roman",10)).grid(row =9,column=1)




#-------------------------------entry------------------------------------------------------------
        input1=Entry(root, width = 28).grid(row = 1,column=2)
        input2=Entry(root, width = 28).grid(row = 2,column=2)
        input3=Entry(root, width = 28).grid(row = 3,column=2)
        input4=Entry(root, width = 28).grid(row = 4,column=2)
        input5=Entry(root, width = 28).grid(row = 5,column=2)
        input6=Entry(root, width = 28).grid(row = 6,column=2)
        input7=Entry(root, width = 28).grid(row = 7,column=2)
        input8=Entry(root, width = 28).grid(row = 8,column=2)
        input9=Entry(root, width = 28).grid(row = 9,column=2)


#------------------------------- mane page button and Functions -------------------------------------------
        def Find():
             lis=[]
             lis.append(input1)
             lis.append(input2)
             lis.append(input3)
             lis.append(input4)
             lis.append(input5)
             lis.append(input6)
             lis.append(input7)
             lis.append(input8)
             lis.append(input9)
             print(lis.min())
             print(lis.max())


            n = len(lis)
            lis.sort()
            if n % 2 == 0:
                median1 = lis[n//2]
                median2 = lis[n//2 - 1]
                median = (median1 + median2)/2
            else:
                median = lis[n//2]
            print("Median is: " + str(median))


            lis.sort() 
            L1=[] 
            i=0
            while i < len(lis) :
                L1.append(lis.count(lis[i]))
                i += 1  
            d1 = dict(zip(lis, L1))  
            d2={k for (k,v) in d1.items() if v == max(L1) }  
            print("Mode is :" + str(d2))




             

        def Reset():
            input1.delete(0,END)
            input2.delete(0,END)
            input3.delete(0,END)
            input4.delete(0,END)
            input5.delete(0,END)
            input6.delete(0,END)
            input7.delete(0,END)
            input8.delete(0,END)
            input9.delete(0,END)


        Button(text="Find",command=Find,bg="#00bd56",fg="white").grid(row = 10,column = 2)
        Button(text="Reset",command=Reset,bg="#ed3833",fg="white").grid(row = 11,column = 2)
     

    elif user=="" and code =="":
        messagebox.showerror("Invalid","please enter correct username and password")
    elif user=="":
        messagebox.showerror("Invalid","username is required ")
    elif code=="":
        messagebox.showerror("Invalid","password is required ")
    elif user! == "Birbal" and code!=="12345":
        messagebox.showerror("Invalid","Invalid username and password ")
    elif user!=="Birbal":
        messagebox.showerror("Invalid","please enter valid name ")
    elif code!=="12345":
        messagebox.showerror("Invalid","please enter valid password ")
        
# Creating tkinter root
root = tk.Tk()
root.title('Login Page')
root.geometry('300x250')


# ---------------------------------label text for title---------------------
ttk.Label(root, text = "Login Page",background = 'Black', foreground ="Red",
		font = ("Times New Roman", 20,"bold")).grid(row = 0, column = 2,padx = 10, pady = 20)

#----------------------------------label-----------------------------------
ttk.Label(root, text ="User_ID",font = ("Times New Roman",10)).grid(row =1,column=1)
ttk.Label(root, text ="Password",font = ("Times New Roman",10)).grid(row =2,column=1)


# ------------------------------------- Entry ----------------------------------------
User_name=Entry(root, width = 28).grid(row = 1,column=2)
Password=Entry(root, width = 28).grid(row = 2,column=2)
# ------------------------------------------- Button -----------------------


def reset():
    User_name.delete(0,END)
    Password.delete(0,END)

Button(text="Login",command=login,bg="#00bd56",fg="white").grid(row = 4,column = 2)
Button(text="Reset",command=reset,bg="#ed3833",fg="white").grid(row = 5,column = 2)



root.mainloop()
