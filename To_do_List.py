import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("To-do List")
root.geometry("500x650")
root.resizable(False,False)

task_list=[]
def  openTaskFile():
    try:
        global task_list
        with open("tasklist.txt","r") as taskfile:
            tasks = taskfile.readlines()

        for task in tasks:
            if task != '\n':
                task_list.append(task)
                listbox.insert(END, task)
    except:
        file = open("tasklist.txt","w")
        file.close()

def addTask():
    task = todo_entry.get()
    todo_entry.delete(0, END)
    if task:
        with open("tasklist.txt", "a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)
    else:
        messagebox.showwarning("Warning", "Task field cannot be empty!")

def delete_selected_item():
    selected_index = listbox.curselection()
    if selected_index:
        listbox.delete(selected_index)

def update_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        new_task = todo_entry.get()
        if new_task:
            task_list[selected_task_index[0]] = new_task
            listbox.delete(selected_task_index[0])
            listbox.insert(selected_task_index[0], new_task)
            todo_entry.delete(0, END)
        else:
            messagebox.showwarning("Warning", "Task field cannot be empty!")
    else:
        messagebox.showwarning("Warning", "Please select a task to edit!")


logo_image = PhotoImage(file="image/todologo.png")
root.iconphoto(False,logo_image)

lbl = Label(root,borderwidth=-1, relief="groove", bd=4, fg="white", bg="blue", width="62", height="5")
lbl.place(x=35, y=10)
lbl = Label(root, text="Orgnaize your time",fg="white",bg="blue", font="arial 15 bold",)
lbl.place(x=160,y=17)

lbl = Label(root, text="more productivity",fg="white",bg="blue", font="arial 15 bold",)
lbl.place(x=165,y=50)

sideimage  = PhotoImage(file="image/bar image 1.png")
Label(root, image=sideimage, width=70, height=60,bg="blue").place(x=45, y=14)

lbl = Label(root, text="Todo Categories",fg="green", font="arial 20 bold")
lbl.place(x=30, y=170)

lbl = Label(root,borderwidth=-1, relief="groove", bd=4, bg="white", width="7", height="3")
lbl.place(x=35, y=227)
schoolimage  = PhotoImage(file="image/school.png")
Label(root, image=schoolimage).place(x=37, y=230)
lblsc = Label(root, text="School",fg="green", font="arial 10",width="8")
lblsc.place(x=27,y=280)


lbl = Label(root,borderwidth=-1, relief="groove", bd=4, bg="white", width="7", height="3")
lbl.place(x=155, y=227)
holidayimage  = PhotoImage(file="image/holidays.png")
Label(root, image=holidayimage).place(x=159, y=232)
lblhl = Label(root, text="Holiday",fg="green", font="arial 10",width="8")
lblhl.place(x=148,y=280)


lbl = Label(root,borderwidth=-1, relief="groove", bd=4, bg="white", width="7", height="3")
lbl.place(x=275, y=227)
businessimage  = PhotoImage(file="image/business.png")
Label(root, image=businessimage).place(x=280, y=230)
lblbs = Label(root, text="Business",fg="green",font="arial 10",width="8")
lblbs.place(x=269,y=280)


lbl = Label(root,borderwidth=-1, relief="groove", bd=4, bg="white", width="7", height="3")
lbl.place(x=395, y=227)
shopingimage  = PhotoImage(file="image/shoping.png")
Label(root, image=shopingimage).place(x=398, y=230)
lblso = Label(root, text="Shoping",fg="green", font="arial 10",width="8")
lblso.place(x=390,y=280)


separator = ttk.Separator(root, orient='horizontal')
separator.place(relx=0, rely=0.53, relwidth=1, relheight=1)

lbl = Label(root, text="Today's Tasks",fg="green", font="arial 15 bold")
lbl.place(x=30, y=350)

frame = Frame(root, width=445, height=52, bg="white")
frame.place(x=30, y=380)

todo=StringVar()
todo_entry=Entry(frame, width=30, font="arial 15", bd=0)
todo_entry.place(x=10, y=7)
todo_entry.focus()
addicon=PhotoImage(file="image/addicon.png")
button = Button(frame, image=addicon, bd=0, command=addTask)
button.place(x=395, y=0)

frame1 = Frame(root, bd=3, width=700, height=59, bg="yellow")
frame1.place(x=30, y=440)
listbox = Listbox(frame1, font=('arial',12), width=40, height=10, bg="yellow")
listbox.pack(side=LEFT, fill=BOTH, padx=2)
scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)
openTaskFile()


deleteicon=PhotoImage(file="image/deleteicon.png")
button = Button(root, image=deleteicon, bd=0, command=delete_selected_item)
button.place(x=425, y=473)
updateicon=PhotoImage(file="image/editicon.png")
button = Button(root, image=updateicon, bd=0, command=update_task)
button.place(x=425, y=550)


root.mainloop()