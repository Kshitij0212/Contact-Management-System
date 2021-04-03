import MySQLdb
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
from tkinter import *

def connection():
    global conn , cursor
    conn = MySQLdb.connect(host='localhost', database='project', password='kshitij@2k', user='root')
    cursor = conn.cursor()

root = Tk()
root.geometry('900x400')
root.title('Contact Management System')

def display_frames():

    #Declaring variables 

    global tree
    global search
    global ID, first_name, last_name, email, gender, contact_no
    search = StringVar()
    ID = StringVar()
    first_name = StringVar()
    last_name = StringVar()
    email = StringVar()
    gender = StringVar()
    contact_no = StringVar()

    #Creating frames

    f1 = Frame(root, width=600, height=100, bg='#78B4F3')
    f1.pack(side=TOP, fill=X)

    f2 = Frame(root, width=450, bg='#031325')
    f2.pack(side=LEFT, fill=Y)

    f3 = Frame(root, width=500, bg='#103357')
    f3.pack(side=LEFT, fill=Y)

    f4 = Frame(root, width=650, bg='green')
    f4.pack(side=RIGHT, fill=Y)

    #Creating widgets in Frame 1

    lbtitle = Label(f1, text="Contact Management System", font='Times 25 bold italic', bg='#78B4F3', fg='#031325')
    lbtitle.pack(pady=25)

    #Creating widgets in Frame 2

    lbfname = Label(f2, text="First Name", font='Arial 20 bold', bg='#031325', fg='#78B4F3')
    lbfname.pack(padx=100, pady=15)

    efname = Entry(f2, width=25, fg='black', bg='white', font='Arial 15', textvariable=first_name)
    efname.pack()

    lblname = Label(f2, text="Last Name", font='Arial 20 bold', bg='#031325', fg='#78B4F3')
    lblname.pack(padx=100, pady=15)

    elname = Entry(f2, width=25, fg='black', bg='white', font='Arial 15', textvariable=last_name)
    elname.pack()

    lbgender = Label(f2, text="Gender", font='Arial 20 bold', bg='#031325', fg='#78B4F3')
    lbgender.pack(padx=100, pady=15)

    sgender = Spinbox(f2, values=('male', 'female', 'other'), fg='black', bg='white', width=20, font='Arial 17', textvariable=gender)
    sgender.pack()

    lbemail = Label(f2, text="Email", font='Arial 20 bold', bg='#031325', fg='#78B4F3')
    lbemail.pack(padx=100, pady=15)

    eemail = Entry(f2, width=25, fg='black', bg='white', font='Arial 15', textvariable=email)
    eemail.pack()

    lbcontact = Label(f2, text="Contact", font='Arial 20 bold', bg='#031325', fg='#78B4F3')
    lbcontact.pack(padx=100, pady=15)

    efcontact = Entry(f2, width=25, fg='black', bg='white', font='Arial 15', textvariable=contact_no)
    efcontact.pack()

    bsubmit = Button(f2, text="Submit", bg='#78B4F3', fg='#031325', font='Arial 20 bold', width=12, command = add_details)
    bsubmit.pack(pady=35)

    #Creating widgets in Frame 3

    lbsearch = Label(f3, text="Enter first name to search", font='Arial 20 bold', bg='#103357', fg='#D0E1F4')
    lbsearch.pack(padx=15, pady=15)

    esearch = Entry(f3, width=30, fg='#103357', bg='white', font='Arial 15', textvariable=search)
    esearch.pack(pady=10)

    bsearch = Button(f3, text="Search", bg='#D0E1F4', fg='#103357', font='Arial 20 bold', width=15, command=search_record)
    bsearch.pack(pady=20)

    bviewall = Button(f3, text="View all", bg='#D0E1F4', fg='#103357', font='Arial 20 bold', width=15, command=display_details)
    bviewall.pack(pady=20)

    breset = Button(f3, text="Reset", bg='#D0E1F4', fg='#103357', font='Arial 20 bold', width=15, command=reset)
    breset.pack(pady=20)

    bdelete = Button(f3, text="Delete", bg='#D0E1F4', fg='#103357', font='Arial 20 bold', width=15, command=delete)
    bdelete.pack(pady=20)

    bupdate = Button(f3, text="Update", bg='#D0E1F4', fg='#103357', font='Arial 20 bold', width=15, command=update)
    bupdate.pack(pady=20)

    #Creating TreeView for Frame 4

    scrollbarx = Scrollbar(f4, orient=HORIZONTAL)
    scrollbary = Scrollbar(f4, orient=VERTICAL)

    tree = ttk.Treeview(f4, columns=('ID', 'first_name', 'last_name', 'email', 'gender', 'contact_no'), height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)

    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)

    tree.heading('ID', text="ID", anchor=CENTER)
    tree.heading('first_name', text="First Name", anchor=CENTER)
    tree.heading('last_name', text="Last Name", anchor=CENTER)
    tree.heading('gender', text="Gender", anchor=CENTER)
    tree.heading('email', text="Email", anchor=CENTER)
    tree.heading('contact_no', text="Contact No.", anchor=CENTER)
    
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=80, anchor=CENTER)
    tree.column('#2', stretch=NO, minwidth=0, width=150, anchor=CENTER)
    tree.column('#3', stretch=NO, minwidth=0, width=150, anchor=CENTER)
    tree.column('#4', stretch=NO, minwidth=0, width=230, anchor=CENTER)
    tree.column('#5', stretch=NO, minwidth=0, width=100, anchor=CENTER)
    tree.column('#6', stretch=NO, minwidth=0, width=150, anchor=CENTER)

    tree.pack()

def add_details():

    connection()

    first_name1 = first_name.get()
    last_name1 = last_name.get()
    gender1 = gender.get()
    email1 = email.get()
    contact_no1 = contact_no.get()

    if (first_name1==' ' or last_name1==' 'or gender1==' ' or email1==' 'or contact_no1==' '):
        tkMessageBox.showinfo("Message","Please fill out the empty fields..")
    else:
        str = "insert into contacts(first_name, last_name, gender, email, contact_no) values('%s', '%s', '%s', '%s', '%s')"
        args = (first_name1, last_name1, gender1, email1, contact_no1)
        cursor.execute(str % args)
        conn.commit()
        tkMessageBox.showinfo("Message","Contact Saved Successfully..!!")

    display_details()
    conn.close()

def display_details():

    connection()
    
    tree.delete(*tree.get_children())

    cursor.execute("select * from contacts")
    fetch = cursor.fetchall()

    for data in fetch:
        tree.insert('','end', values=(data))
        tree.bind("<Double-1>", OnDoubleClick)

    conn.close()

def delete():

    connection()

    if not tree.selection():
        tkMessageBox.showwarning("Warning","Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            current_item = tree.focus()
            contents = (tree.item(current_item))
            selected_item = contents['values']
            tree.delete(current_item)
            str = "delete from contacts where ID = '%d'"
            args = (selected_item[0])
            cursor.execute(str % args)
            conn.commit()

    reset()

    cursor.close()
    conn.close()

def reset():

    tree.delete(*tree.get_children())
    display_details()
    
    search.set("")
    first_name.set("")
    last_name.set("")
    gender.set("")
    email.set("")
    contact_no.set("")
 
def search_record():
    
    connection()
    
    search1 = search.get()

    if search1 != "":
        
        tree.delete(*tree.get_children())
        
        str = "select * from contacts where first_name = '%s'"
        args = (search1)
        cursor.execute(str % args)
        fetch = cursor.fetchall()
        
        for data in fetch:
            tree.insert('', 'end', values=(data))
            tree.bind("<Double-1>", OnDoubleClick)

        cursor.close()
        conn.close()

def update():

    connection()
    
    first_name1 = first_name.get()
    last_name1 = last_name.get()
    gender1 = gender.get()
    email1 = email.get()
    contact_no1 = contact_no.get()
    
    if (first_name1=='' or last_name1==''or gender1=='' or email1==''or contact_no1==''):
        tkMessageBox.showinfo("Message","Please fill the required details.")
    else:
   
        current_item = tree.focus()
        contents = (tree.item(current_item))
        selected_item = contents['values']
        
        str = "update contacts set first_name = '%s', last_name = '%s', gender = '%s', email = '%s', contact_no = '%s'  where ID = '%d'"
        args = (first_name1, last_name1,gender1,email1,contact_no1, selected_item[0])
        cursor.execute(str % args)
        
        conn.commit()
        tkMessageBox.showinfo("Message","Updated successfully")
       
        reset()
        
        display_details()
        conn.close()

def OnDoubleClick(self):

    current_item = tree.focus()             
    contents = (tree.item(current_item))   
    selected_item = contents['values']      

    ID.set(selected_item[0])
    first_name.set(selected_item[1])
    last_name.set(selected_item[2])
    email.set(selected_item[3])
    gender.set(selected_item[4])
    contact_no.set(selected_item[5])

display_frames()
if __name__=='__main__':
    root.mainloop()
