import tkinter as tk

root = tk.Tk()

root.title("Marvellous Circle Area Calculator")
root.geometry("400x300")

tk.Label(root,text="Marvellous Infosystems",
         font=("Arial",18,"bold")).pack(pady=10)

tk.Label(root,text="Enter Radius").pack()
entry1 = tk.Entry(root)
entry1.pack()

def Area():
    no1 = int(entry1.get())

    result = 3.14 * no1 * no1

    labelResult.config(text = "Area of Circle is : "+str(result))
    
tk.Button(root,text="Area",command=Area).pack(pady=15)

labelResult = tk.Label(root,text="",font=("Arial",14))
labelResult.pack()

root.mainloop()                                
