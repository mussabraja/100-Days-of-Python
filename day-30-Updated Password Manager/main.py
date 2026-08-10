import tkinter
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)
    password_list =  [random.choice(letters) for char in range(nr_letters)]
    password_list += [random.choice(symbols) for char in range(nr_symbols)]
    password_list += [random.choice(numbers) for d in range(nr_numbers)]
    random.shuffle(password_list)
    password = "".join(password_list)
    input_password.delete(0, END)
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = input_website.get()

    try:
        with open("data.json",'r') as f:
            data = json.load(f)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found")
    else:
        if website in data:
            email = data[website]["email"]
            passs = data[website]["password"]
            messagebox.showinfo(title="Confirm", message= f'Your email:{email} and password:{passs}')
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists")







# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = input_website.get()
    password = input_password.get()
    email = input_username.get()

    new_data = {
        website:{"email":email,
                 "password":password,
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title='Warning',message="Empty Field")
    else:
            #Read old data
            try:
                with open("data.json", "r") as data_file:
                    data = json.load(data_file)
            #Update old data with new data
            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    json.dump(new_data, data_file)
            else:
                data.update(new_data)
                with open("data.json","w") as data_file:
                    json.dump(data,data_file)
            finally:
                input_website.delete(0, END)
                input_username.delete(0, END)
                input_password.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title('Password Generator by Mussab')
window.minsize(width=200,height=300)
window.config(padx=50,pady=50)
canvas = Canvas(width=200,height=200)
photo = PhotoImage(file='logo.png')
canvas.create_image(100,100,image = photo)
canvas.grid(row=0,column=1)
label_website = tkinter.Label(text='Website: ')
label_website.grid(column=0,row=1)
label_email = tkinter.Label(text='Email/ Username ')
label_email.grid(column=0,row=2)
label_password = tkinter.Label(text='Password')
label_password.grid(column=0,row=3)
input_website = Entry(width=24)
input_website.grid(column=1,row=1,columnspan=2)
input_username = Entry(width=35)
input_username.grid(column=1,row=2,columnspan=2)
input_password = Entry(width=25)
input_password.grid(column=1,row=3)
button_generate_password = Button(text='Generate Password ',command=gen_password)
button_generate_password.grid(column=2,row=3)
button_add = Button(text='Add ',width=36,command=save)
button_add.grid(row=4,column=1,columnspan=2)
button_search = Button(text='Search',command=find_password)
button_search.grid(column=2,row=1)
input_website.focus()
input_username.insert(0,'mussab@gmail.com')
window.mainloop()