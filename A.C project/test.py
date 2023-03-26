import tkinter as tk 

class test_gui:
    def __init__(self):
        self.root = tk.Tk()

        self.root.geometry("800x500")
        self.root.title("A.C")

        self.label = tk.Label(self.root, text= "Test Your Button!", font = ("Arial", 18))
        self.label.pack(padx = 10, pady = 10)

        self.textbox = tk.Text(self.root, height = 5, font = ("Arial", 16))
        self.textbox.pack(padx = 10, pady = 10)

        self.check_state = tk.IntVar()

        self.checkbutton = tk.Checkbutton(self.root, text = "Check Here!", font= ("Arial", 16), variable= self.check_state)
        self.checkbutton.pack(padx= 10, pady= 10)

        self.button = tk.Button(self.root, text = "Click!", font = ("Arial", 18), command= self.show_message)
        self.button.pack(padx = 10, pady = 10)
        self.root.mainloop()
    
    def show_message(self):
        if self.check_state == 1:
            print("Thank You!")
        else:
            print("welp")


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