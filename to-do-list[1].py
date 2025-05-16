import tkinter as tk
from tkinter import messagebox
def add_task():
    task=entry.get()
    if task:
       listbox.insert(tk.END,task)
       entry.delete(0,tk.END)
    else:
      messagebox.showwarning("warning")
def mark_task():
 try:
    selected=listbox.curselection()[0]
    task=listbox.get(selected)
    listbox.delete(selected)
    listbox.insert(tk.END,f"correct{task}")
 except IndexError:
    messagebox.showwarning("warning")
def delete_task():
    try:
        selected=listbox.curselection()[0]
        listbox.delete(selected)
    except IndexError:
       messagebox.showwarning("warning")
root=tk.Tk()
root.title("to-do-list")
entry=tk.Entry(root,width=40)
entry.pack()
button=tk.Button(root,text="addtask",command=add_task)
button.pack()
listbox=tk.Listbox(root,width=40,height=20)
listbox.pack()
mark_button=tk.Button(root,text="markdone",command=mark_task)
mark_button.pack()
delete_button=tk.Button(root,text="deletetask",command=delete_task)
delete_button.pack()
root.mainloop()
