import tkinter as tk 
from tkinter import messagebox

class test_gui:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("A.C")

        self.label = tk.Label(self.root, text= "Test Your Button!", font = ("Arial", 18))
        self.label.pack(padx = 10, pady = 10)

        self.textbox = tk.Text(self.root, height = 5, font = ("Arial", 16))
        self.textbox.pack(padx = 10, pady = 10)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.check_state = tk.IntVar()

        self.checkbutton = tk.Checkbutton(self.root, text = "Check Here!", font= ("Arial", 16), variable= self.check_state)
        self.checkbutton.pack(padx= 10, pady= 10)

        self.button = tk.Button(self.root, text = "Click!", font = ("Arial", 18), command= self.show_message)
        self.button.pack(padx = 10, pady = 10)
        
        self.root.protocol("WM_DELETE_WINDOW", self.leaving_msg)

        self.root.mainloop()
    
    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get("1.0", tk.END))
        else:
            messagebox.showinfo(title = "Message", message = self.textbox.get("1.0", tk.END))

    def shortcut(self, event):
        if event.keysym == "Return" and event.state == 4:
            self.show_message()

    def leaving_msg(self):
        if messagebox.askyesno(title = "Warning!", message = "Do you really want to quit?"):
            self.root.destroy()
        #messagebox.showinfo(title = "Warning!", message = "Are you sure you want to leave?")
        
test_gui()

#root = tk.Tk()

#root.geometry("500x500")
#root.title("A.C")

#label = tk.Label(root, text = "Test Text!", font = ("Arial",18))
#label.pack(padx=20, pady= 20)

#textbox = tk.Text(root, height = 3, width= 12, font= ("Arial", 12))
#textbox.pack()

#checkbutton = tk.Checkbutton(root, text = "test2", font = ("Arial", 14))
#checkbutton.pack(padx=10, pady = 10)


#root.mainloop()