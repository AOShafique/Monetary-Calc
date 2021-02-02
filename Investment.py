import tkinter as tk
import tkinter.ttk as ttk
root = tk.Tk()
root.title("My investment")

inv = tk.Label (root,text ="Investment:",font = ("Times New Roman" , 14))
inv.grid(row = 0 , column = 0)
               
invest = ttk.Combobox(root,text = 0)
invest['values'] = (1000,5000,10000,20000,50000,100000)
invest.grid(row=0,column=1)


dte = tk.Label (root,text ="Date:",font = ("Times New Roman" , 14))
dte.grid(row = 1 , column = 0)

date = tk.Spinbox(root,from_=1,to =31,width = 20)
date.grid(row =1 , column = 1)



mnth = tk.Label (root,text ="Month:",font = ("Times New Roman" , 14))
mnth.grid(row = 1 , column = 3)

month = tk.Spinbox(root,from_=1,to =12,width = 20)
month.grid(row =1 , column = 4)


yr = tk.Label (root,text ="Year:",font = ("Times New Roman" , 14))
yr.grid(row = 1 , column = 6)

year = tk.Spinbox(root,from_=2000,to =2025,width = 20)
year.grid(row =1 , column = 7)

inter = tk.Label (root,text ="Interest percentage:",font = ("Times New Roman" , 14))
inter.grid(row = 2 , column = 0)

interest = ttk.Combobox(root)
interest['values'] = (10,20,30,40,50,60,70,80,90,100)
interest.grid(row=2,column=1)

def calc():
    ip = int(invest.get())*int(interest.get())
    amt = int(ip)/100
    matamt = int(invest.get()) + amt
    matyr = int(year.get()) +1

    mat = tk.Label(root, text = f"Your matured amount = {matamt}/-",font = ("Times New Roman" , 14))
    mat.grid(row=5,column=0)
    matdte = tk.Label(root,text = f"Date: {date.get()}   Month: {month.get()}   Year: {matyr}",font = ("Times New Roman" , 14))
    matdte.grid(row = 6 , column = 0)
    


bt = tk.Button(root,text = "Proceed",font = ('Times New Roman',14), command = calc)
bt.grid(row=3,column = 7)

root.geometry('700x500')


root.mainloop()