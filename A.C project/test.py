import tkinter as tk 

class test_gui:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text= "Test Your Button!", font = ("Arial", 18))
        self.lab
        pass
root = tk.Tk()

root.geometry("500x500")
root.title("A.C")

label = tk.Label(root, text = "Test Text!", font = ("Arial",18))
label.pack(padx=20, pady= 20)

textbox = tk.Text(root, height = 3, width= 12, font= ("Arial", 12))
textbox.pack()

checkbutton = tk.Checkbutton(root, text = "test2", font = ("Arial", 14))
checkbutton.pack(padx=10, pady = 10)


root.mainloop()