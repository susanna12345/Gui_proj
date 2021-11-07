import tkinter as tk
import tkinter.messagebox as msg
    #msg.showinfo("Warning!","Please write a number")
win=tk.Tk()
win.title("Converter")
win.geometry("400x300+750+250")                                           
c=0
def dram():
    try:
        d = float(int(B1.get())*477.25)
    except:
        msg.showinfo("Error!","Please write a number")
    B3['text'] = d

l1 = tk.Label(text = "USD:")
l2 = tk.Label(text = "AMD:")

B1=tk.Entry(text="",fg="green",bg="light blue",width=30,)
B2=tk.Button(text="Convert",fg= "green",bg="light blue",command=dram)
B3=tk.Label(fg="green",bg="light blue",width=30)
l1.place(x= 55, y = 1)
l2.place(x= 55, y = 45)
B1.pack()
B2.pack()
B3.pack()
win.mainloop()