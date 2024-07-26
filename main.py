from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password) 


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website_input= website_entry.get()
    email_input= email_entry.get()
    password_input= password_entry.get()
    
    if website_input == "" or password_input == "":
        messagebox.showerror(title="Oops!", message= "Please Check all entry is filled")
    else:
        IS_ok= messagebox.askokcancel(title= "Website", message= f"The details: \nWebsite: {website_input} \nEmail: {email_input} \nPassword: {password_input} \nIs it ok to save?" )    
        if IS_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website_input} | {email_input} | {password_input} \n")
    website_entry.delete(0,END)
    password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window= Tk()
window.title("Password Manager")

window.config(padx=50, pady= 50)
canvus = Canvas(height=200, width= 200)
password_image= PhotoImage(file= "logo.png")
canvus.create_image(100, 100, image= password_image)
canvus.grid(row=0, column=1)

website_label= Label(text= "Website:")
website_label.grid(row=1, column=0)
website_entry = Entry(width=40)
website_entry.grid(row= 1, column=1, columnspan=4)
website_entry.focus()


email_label = Label(text= "Email/Username:")
email_label.grid(row=2, column=0)
email_entry= Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=4)
email_entry.insert(0, "subha@123.com")



password_label= Label(text="Password:")
password_label.grid(row=3, column=0)
password_entry= Entry(width = 22)
password_entry.grid(row=3, column=1)


generate_button= Button(text="Generate Password", command= password_generate)
generate_button.grid(row=3, column=2)
add_button= Button(text = "Add", width=34, command=save_password)
add_button.grid(row=4, column=1, columnspan=2)




window.mainloop()

