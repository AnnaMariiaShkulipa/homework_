import requests
import json


url="https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user=21&balance=320493"
get_url="https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user=21"
res=requests.get(url)
json=res.json()

res2=requests.get(get_url)
json_get=res2.json()
import tkinter as tk
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import showerror


connection=sqlite3.connect('sqlite.db')
c=connection.cursor()

def view_users():
    print('Users list: \n')
    c.execute('SELECT * FROM user')
    
window=tk.Tk()
window.title('My app')
window.minsize(width=300,height=300)
window.maxsize(width=500,height=500)
#window.geometry('500x300')

def text():
    label['text']=entry.get()
    text.insert(tk.END,entry.get())

    def info():
        messagebox.showerror('info')

label=tk.Label(text='id',bg='white')
label.pack()
entry=tk.Entry(bg='white')
entry.pack()

label2=tk.Label(text='name',bg='white')
label2.pack()
entry2=tk.Entry(bg='white')
entry2.pack()

label3=tk.Label(text='surname',bg='white')
label3.pack()
entry3=tk.Entry(bg='white')
entry3.pack()

label4=tk.Label(text='email',bg='white')
label4.pack()
entry4=tk.Entry(bg='white')
entry4.pack()

label5=tk.Label(text='school_group',bg='white')
label5.pack()
entry5=tk.Entry(bg='white')
entry5.pack()

label6=tk.Label(text='balance',bg='white')
label6.pack()
entry6=tk.Entry(bg='white')
entry6.pack()

def api():
 if json['i']["id"] is None:
          label.config(text = "Error")
 else:
          label.config(text = json)
        
text=tk.Text(width=40,height=40,wrap='word')
scrollbar=Scrollbar(orient=VERTICAL,command=text.yview)
scrollbar.pack(side='right',fill='y')
text.configure(yscrollcommand=scrollbar.set)
text.pack()

window.mainloop()


