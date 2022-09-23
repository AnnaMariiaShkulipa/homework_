import requests
import tkinter
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

label=tk.Label(text='track',bg='white')
label.pack()
entry=tk.Entry(bg='white')
entry.pack()

button=tk.Button(text="click",bg='white',command=text)
button.pack()

url = "https://spotify81.p.rapidapi.com/track_lyrics"

querystring = {"id":"1brwdYwjltrJo7WHpIvbYt"}

headers = {
	"X-RapidAPI-Key": "e1d0bd8defmsh47dc397634e8ef1p1e310ejsn03c6759b7636",
	"X-RapidAPI-Host": "spotify81.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

text=tk.Text(width=40,height=40,wrap='word')
scrollbar=Scrollbar(orient=VERTICAL,command=text.yview)
scrollbar.pack(side='right',fill='y')
text.configure(yscrollcommand=scrollbar.set)
text.pack()

window.mainloop()
