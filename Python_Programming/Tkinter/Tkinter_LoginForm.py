import tkinter as tk

root = tk.Tk()

root.title("Marvellous Login Form")
root.geometry("600x400")

tk.Label(root,text="Marvellous Infosystems",
         font=("Arial",18,"bold")).pack(pady=10)

tk.Label(root,text="Enter your username").pack()
entry1 = tk.Entry(root)
entry1.pack()

tk.Label(root,text="Enter your password").pack()
entry2 = tk.Entry(root)
entry2.pack()

def Check():
    no1 = str(entry1.get())
    no2 = str(entry2.get())

    if no1 == "marvellous@123" and no2 == "123456":
        labelResult.config(text = "Login Successful")
    else:
        labelResult.config(text = "Login Failed")

tk.Button(root,text="Login",command=Check).pack(pady=15)

labelResult = tk.Label(root,text="",font=("Arial",14))
labelResult.pack()

root.mainloop()



