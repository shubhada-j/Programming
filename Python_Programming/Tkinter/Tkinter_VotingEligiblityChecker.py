import tkinter as tk

root = tk.Tk()

root.title("Marvellous Voting Eligiblity Checker Calculator")
root.geometry("400x300")

tk.Label(root,text="Marvellous Infosystems",
         font=("Arial",18,"bold")).pack(pady=10)

tk.Label(root,text="Enter your Age").pack()
entry1 = tk.Entry(root)
entry1.pack()

def Checker():
    no1 = int(entry1.get())

    if no1 >= 18:
        labelResult.config(text = "You are Eligible")
    else:
        labelResult.config(text = "You are not Eligible")

tk.Button(root,text="Voting Eligiblity Checker",command=Checker).pack(pady=15)

labelResult = tk.Label(root,text="",font=("Arial",14))
labelResult.pack()

root.mainloop()                                         