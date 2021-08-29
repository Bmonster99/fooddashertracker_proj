from tkinter import *
import dashbe

def gsr(event):
    try:
    
        
        global st
        index = list1.curselection()[0]
        st = list1.get(index)
        e1.delete(0,END)
        e1.insert(END, st[1])
        e2.delete(0,END)
        e2.insert(END, st[2])
        e3.delete(0,END)
        e3.insert(END, st[3])
        e4.delete(0,END)
        e4.insert(END, st[4])
    except IndexError:
        pass
   

def view_cmd():
    list1.delete(0, END)
    for row in dashbe.view():
        list1.insert(END, row)

def search_cmd():
    list1.delete(0, END)
    for row in dashbe.search(Bag_text.get(), Miles_text.get(), Hours_text.get(), Date_text.get()):
        list1.insert(END, row)

def add_cmd():
    dashbe.insert(Bag_text.get(), Miles_text.get(), Hours_text.get(), Date_text.get())
    list1.delete(0, END)
    list1.insert(END, (Bag_text.get(), Miles_text.get(), Hours_text.get(), Date_text.get()))

    

def delete_cmd():
  
    dashbe.delete(st[0])


def update_cmd():
    
    dashbe.edit(st[0], Bag_text.get(), Miles_text.get(), Hours_text.get(), Date_text.get())



window = Tk()

window.title("Dasher's Bag")



 # gui ui labels

l1 = Label(window, text = " Money Bag")
l1.grid(row = 0, column = 0)

l2 = Label(window, text = "Miles Driven")
l2.grid(row = 1, column = 0) 

l3 = Label(window, text = "Hours Worked")
l3.grid(row = 0, column = 2)

l4 = Label(window, text = "Date")
l4.grid(row = 1, column = 2)

# gui entries

Bag_text = StringVar()
e1 = Entry(window, textvariable = Bag_text)
e1.config(width = 7)
e1.grid(row = 0, column = 1)

Miles_text = StringVar()
e2 = Entry(window, textvariable = Miles_text)
e2.config(width = 7)
e2.grid(row = 1, column = 1)


Hours_text = StringVar()
e3 = Entry(window, textvariable = Hours_text)
e3.config(width = 7)
e3.grid(row = 0, column = 3)

Date_text = StringVar()
e4 = Entry(window, textvariable = Date_text)
e4.config(width = 7)
e4.grid(row = 1, column = 3)


# buttons

b1 = Button(window, text = "View", width = 12, command = view_cmd)
b1.grid(row = 4, column = 0)

b2 = Button(window, text = "Add", width = 12, command = add_cmd)
b2.grid(row = 5, column = 0)

b3 = Button(window, text = "Delete", width = 12, command = delete_cmd)
b3.grid(row = 4, column = 1)

b4 = Button(window, text = "Edit", width = 12, command = update_cmd)
b4.grid(row = 5, column = 1)

b5 = Button(window, text = "Search Dash", width = 12, command = search_cmd)
b5.grid(row = 6, column = 0)


# listbox
list1 = Listbox(window, height = 6, width = 20)
list1.grid(row = 3, column = 2, rowspan = 6, columnspan = 2)

# scrollbar

sb1 = Scrollbar(window)
sb1.grid(row = 3, column = 12, rowspan = 6)

list1.configure(yscrollcommand = sb1.set)
sb1.configure(command = list1.yview)

list1.bind('<<ListboxSelect>>', gsr)





window.mainloop()