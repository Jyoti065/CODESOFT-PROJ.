from tkinter import *
import random
import pyperclip

tk=Tk()
tk.geometry('300x300')
tk.configure(background='#CBC3E3')

pswd=StringVar()
passlen=IntVar()
passlen.set('')

def password_generator():
    characters='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890 !@#$%^&*()'
    password=''
    if passlen.get()>=4:
        for i in range(passlen.get()):
            password+=random.choice(characters)
        pswd.set(password)

def copyclipboard():
    random_password = pswd.get()
    pyperclip.copy(random_password)
    Label(tk,text="Copied to Clipboard",bg="gray").pack(pady=7)

Label(tk, text="Strong Password Generator", font="Arial",bg='#A5C7E5',fg='black').pack(pady=2)
Label(tk, text="Enter your desired  length of password\n(Minimum length should be 6)",font="Courier 8 bold",bg='#FFF5EE',fg='black').pack(pady=4)
Entry(tk, textvariable=passlen).pack(pady=9,ipadx=4)
Button(tk, text="Generate Password", command=password_generator,bg='aliceblue',fg='black').pack(pady=7)
Entry(tk, textvariable=pswd).pack(pady=9,ipadx=4)
Button(tk, text="Copy to clipboard", command=copyclipboard,bg='aliceblue',fg='black').pack(pady=7)

# To initiate and display the root window we created
tk.mainloop()