from curses import window
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
#Storage in memory

def add_contact() -> None:
    #Take the value and typing in text.name
    name = text.name.get()
    phone = text.phone.get()
    category = text.category.get()
    contact = {
        "name": name,
        "phone": phone,
        "category": category
    }
    phonebook.append(contact)
    clear_camp()
    update_table()
    messagebox.showinfo("New Contact", "New Contact Added")
def clear_camp() -> None:
    #clear all camps information
    text.name.delete(0, END)
    text.phone.delete(0, END)
    cb_category.set("")
def edit_contact() -> None:
    #Take the value and typing in text.name
    name = text.name.get()
    phone = text.phone.get()
    category = cb_category.get()
    contact = {
        "name": name,
        "phone": phone,
        "category": category
    }
    for i in range(len(phonebook)):
        if phonebook[i]["name"] == name:
            phonebook[i] = contact
            messagebox.showinfo("Edit Contact", "Contact Edited")
            clear_camp()
            update_table()
            break
    else:
        messagebox.showinfo("Edit Contact", "Contact Not Found")
def delete_contact() -> None:
    #Delete the contact
    name = text.name.get()
    for i in range(len(phonebook)):
        if phonebook[i]["name"] == name:
            del phonebook[i]
            messagebox.showinfo("Delete Contact", "Contact Deleted")
            clear_camp()
            update_table()
            break
def update_table() -> None:
    #Update the table
    for line in table.get_children():
       table.delete(line)
    for contact in phonebook:
        table.insert("", END, values =(contact["name"],
                                       contact["phone"],
                                       contact["category"]))
def table_click(event) -> None:
    #obtain the line click event
    selected_line = table.selection()
    global index
    index = table.index(selected_line[0])
    contact = phonebook[index]
    clear_camp()
    text_name.insert(0, contact["name"])
    text_phone.insert(0, contact["phone"])
    cb_category.set(contact["category"])
    
    window(tk)
    window.title("phonebook")
    
lable_name = Label(window, text="name", foreground="red", font="Tahoma 14 bold")
lable_name.grid(row=0, column=0)
    
    #Entry
    
text_name = Entry(window, font="Tahoma 14", width=27)
text_name.grid(row=0, column=1)
    
lable_phone = Label(window, text="phone", foreground="red", font="Tahoma 14 bold")
lable_phone.grid(row=1, column=0)
    
    #Entry
    
text_phone = Entry(window, font="Tahoma 14", width=27)
text_phone.grid(row=1, column=1)
    
label_phone = Label(window, text="Phone", foreground="red", font="Tahoma bold 14")
    
    #ComboBox
    
label_category = Label(window, text="category", foreground="red", font="Tohoma 14 bold")
label_category.grid(row=2, column=0)
    
categories = ["Frieds", "Family", "job"]
cb_categories = ttk.Combobox (window, values = categories, width = 25, font = "Tahoma 14 bold")
cb_categories.grid(row=2, column=1)

    #Button

btn_add = Button(window, text= "Add", foreground="red", font="Tahoma 12 bold", width=8, command=add_contact)
btn_add.grid(row=3, column=0)

btn_edit = Button(window, text= "Edit", foreground="red", font="Tahoma 12 bold", width=8, command=edit_contact)
btn_edit.grid(row=3, column=1)

btn_delete = Button(window, text= "Delete", foreground="red", font="Tahoma 12 bold", width=8, command=delete_contact)
btn_delete.grid(row=3, column=2)

columns = ["name", "phone", "category"]

    #Create a table/treeview style

table = ttk.Treeview(window, columns = columns, show = "headings")
for column in columns:
    table.heading(column, text=column)
table.grid(raw=4, columnspan=3)
    
    # Create a Bind

table.bind("<ButtonRelease-1>", table_click)
update_table.bind("Buttom release-1", table_click)

#Run a window   
     
window.mainloop()