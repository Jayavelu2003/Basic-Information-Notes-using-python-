# Import Module
from tkinter import *

# Create Object
root = Tk()
root.title("Basic Information Notes")

# Set geometry
root.geometry('400x500')

# Information List
datas = []

# Add Information
def add():
	global datas
	datas.append([Name.get(),Id.get(),Number.get(),email.get(),address.get()])
	update_book()

# View Information
def view():
	Name.set(datas[int(select.curselection()[0])][0])
	Id.set(datas[int(select.curselection()[0])][1])
	Number.set(datas[int(select.curselection()[0])][2])
	email.set(datas[int(select.curselection()[0])][3])
	address.set(datas[int(select.curselection()[0])][4])

# Delete Information
def delete():
	del datas[int(select.curselection()[0])]
	update_book()

def reset():
	Name.set('')
	Id.set('')
	Number.set('')
	email.set('')
	address.set('')
                
# Update Information
def update_book():
	select.delete(0,END)
	for n,i,p,e,a in datas:
		select.insert(END, n)

# Add Buttons, Label, ListBox
Name = StringVar()
Id =StringVar()
Number = StringVar()
email=StringVar()
address=StringVar()

frame = Frame()
frame.pack(pady=15)

frame4 = Frame()
frame4.pack(pady=15)

frame1 = Frame()
frame1.pack(pady=15)

frame2 = Frame()
frame2.pack(pady=15)

frame3 = Frame()
frame3.pack(pady=15)

Label(frame, text = 'Name:', font='arial 12 bold').pack(side=LEFT)
Entry(frame, textvariable = Name,width=50).pack()

Label(frame4, text = 'ID:', font='arial 12 bold').pack(side=LEFT)
Entry(frame4, textvariable = Id,width=50).pack()

Label(frame1, text = 'Phone No:', font='arial 12 bold').pack(side=LEFT)
Entry(frame1, textvariable = Number,width=50).pack()

Label(frame2, text = 'E-mail:', font='arial 12 bold').pack(side=LEFT)
Entry(frame2, textvariable = email,width=50).pack()

Label(frame3, text = 'Address:', font='arial 12 bold').pack(side=LEFT)
Entry(frame3, textvariable = address,width=50).pack()

Button(root,text="Add",font="arial 12 bold",command=add).place(x= 100, y=270)
Button(root,text="View",font="arial 12 bold",command=view).place(x= 100, y=310)
Button(root,text="Delete",font="arial 12 bold",command=delete).place(x= 100, y=350)
Button(root,text="Reset",font="arial 12 bold",command=reset).place(x= 100, y=390)

scroll_bar = Scrollbar(root, orient=VERTICAL)
select = Listbox(root, yscrollcommand=scroll_bar.set, height=12)
scroll_bar.config (command=select.yview)
scroll_bar.pack(side=RIGHT, fill=Y)
select.place(x=200,y=270)

# Execute Tkinter
root.mainloop()
