from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#Storage in memory

def add_contact() -> None:
#Take the value and typing in txt_name
    name = txt_name.get()
    phone = txt_phone.get()
    category = cb_categories.get()
    contact = {
        'name': name,
        'phone': phone,
        'category': category
    }
    contact_list.append(contact)
    clear_camps()
    update_table()
    messagebox.showinfo('Sucess!', 'New contact added')

def clear_camps() -> None:
#Clear the camps
    txt_name.delete(0, END)
    txt_phone.delete(0, END)
    cb_categories.set("")

def edit_contact() -> None:
    pass
#Take the value and typing in the txt_name
    name = txt_name.get()
    phone = txt_name.get()
    category = cb.categories
    contact = {'name': name,
               'phone': phone,
               'category': category
    }
    for i in range(len(agenda)):
        if agenda[i]['name'] == name:
            agenda[i] = contact
            messagebox.showinfo('Edit contact', 'Contact edited!')
            clear_camps()
            update_table()
            break
        else:
            messagebox.showinfo('Edit contact','Contact not found!')
def delete_contact() -> None:
    pass
#     name = txt_name.get()
#     for i in range(len(agenda)):
#         if agenda[i]['name'] == name:
#             del agenda[i]
#             messagebox.showinfo('Delete contact', 'Contact deleted!')
#             clear_camps()
#             update_table()
#             break
def update_table() -> None:
    for line in table.get_children():
        table.delete(line)
    for contact in contact_list:
        table.insert("", END, values=(contact['name'],
                                      contact['phone'],
                                      contact['category']))
def tabela_click(event) -> None:
#Obtein the line click event
    selected_line = table.selection()
    global index
    index = table.index(selected_line[0])
    contact = contact_list[index]
    clear_camps()
    txt_name.insert(0, contact['name'],)
    txt_phone.insert(0, phone['phone'])
    cb_categories.set(contact['category'])

window = Tk()
window.title('Contact List')

label_name = Label(window, text="Name:", fg="red", font="Tahoma 14 bold")
label_name.grid(row=0, column=0)

# Entry
txt_name = Entry(window, font="Tahoma 14", width=27)
txt_name.grid(row=0, column=1)

label_phone = Label(window, text="Phone:", fg="red", font="Tahoma 14 bold")
label_phone.grid(row=1, column=0)

# Entry
txt_phone = Entry(window, font="Tahoma 14", width=27)
txt_phone.grid(row=1, column=1)

# Combobox

label_categories = Label(window, text="Category:", fg="red", font="Tahoma 14 bold")
label_categories.grid(row=2, column=0)

categories = ["Friend", "Family", "Job"]
cb_categories = ttk.Combobox(window, values=categories, width=25, font="Tahoma 14")
cb_categories.grid(row=2, column=1)

# botão
btn_add = Button(window, text="Add", fg="red",
                       font="Tahoma 12 bold", width=8, command=add_contact())
btn_add.grid(row=3, column=0)

btn_edit = Button(window, text="Edit", fg="red",
                    font="Tahoma 12 bold", width=8, command=edit_contact())
btn_edit.grid(row=3, column=1)

btn_delete = Button(window, text="Delete", fg="red",
                     font="Tahoma 12 bold", width=8, command=delete_contact())
btn_delete.grid(row=3, column=2)

columns = ["Name", "Phone", "Category"]

# Create a TreeView table
table = ttk.Treeview(window, columns=columns, show="headings")
for column in columns:
    table.heading(column, text=column)

table.grid(raw=4, columnspan=3)

#Create a bind
table.bind('ButtonRelease-1', tabela_click)

#Run a window
window.mainloop()
