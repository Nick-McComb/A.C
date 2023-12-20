import tkinter as tk 
from tkinter import PhotoImage
from tkinter import messagebox
from PIL import Image, ImageTk
import win32api 
import win32con
import time
from threading import Thread
import keyboard
 
class AC:
    def __init__(self):
        
        #self.keybind = None
        #self.keybind_bind = None
        self.cps = None
        self.val = 1
        
        self.root = tk.Tk()
        self.root.title("A.C")
        self.root.geometry("400x700")
        
        #self.bg = PhotoImage(file = "C:\\Users\\NickM\\Desktop\\A.C\\A.C_project\\goku2.png")
        #self.bg = ImageTk.PhotoImage(Image.open("C:\\Users\\NickM\\Desktop\\A.C\\A.C_project\\goku2.png"))
        #self.label = tk.Label(self.root, image = self.bg)
        #self.label.place(x= 0, y = 0, relwidth= 1, relheight= 1)

        self.image = Image.open("C:\\Users\\NickM\\Desktop\\A.C\\goku2.png")
        self.rs_image = self.image.resize((400, 700),Image.ANTIALIAS )
        self.bg = ImageTk.PhotoImage(self.rs_image)

        self.canvas = tk.Canvas(self.root, width= 400, height = 700)
        self.canvas.pack(fill = "both", expand = True)
        self.canvas.create_image(0,0, image = self.bg, anchor = "nw")
        #self.canvas.bind("<KeyPress>", self.start_short)
        #self.root.configure(background=  self.bg)
        #self.color_scale = Image.open("C:\\Users\\NickM\\Desktop\\A.C\\color.png")
        #self.rs_color_scale = self.image.resize((250, 20),Image.ANTIALIAS)
        self.choose = tk.Label(self.root, text = "Choose Cps", font = ("Arial, 16"), width = 9, height = 1, bg = "#F6F6F6")
        self.choose_window = self.canvas.create_window(200, 40, anchor = 'n', window = self.choose)

        self.slider = tk.Scale(self.root, from_ = 0, to = 20, resolution = 1, orient= "horizontal",tickinterval=20, width = 20, length = 250, borderwidth= 2, troughcolor='#1065BF',bg ="white", relief="solid",command = self.choose_cps)
        self.slider_window = self.canvas.create_window(200, 74, anchor = "n", window = self.slider)

        self.select_btn = tk.Button(self.root, text= "Select",font =("Arial",18),relief="solid",borderwidth=2,bg="white", command = self.step) #command = lambda:[self.start_click, self.stop_btn])
        self.select_btn_window = self.canvas.create_window(200,200, anchor= "n", window = self.select_btn)
        #self.select_btn.bind("<KeyPress>",self.start_short)
        self.clear_btn = tk.Button(self.root, text = "Clear", font = ("Arial",12), height=1 , width= 4,borderwidth=2, bg= "white",relief= "solid", command= self.clear)
        self.clear_btn_window = self.canvas.create_window(240, 159, anchor = "n", window = self.clear_btn)

        self.stop_btn = tk.Button(self.root, text ="Stop", font = ("Arial", 18),bg = "white", borderwidth=2,relief="solid", command = self.stop_click)
        self.stop_btn_window = self.canvas.create_window(200, 250, anchor= "n", window = self.stop_btn)
        #self.stop_btn.bind("<KeyPress>",self.stop_short)

        self.textbox = tk.Text(self.root, height= 1, width= 1, font = ("Arial", 16), relief="solid", borderwidth=2)
        self.textbox_window = self.canvas.create_window(200,160, anchor = "n", window = self.textbox)
        #self.root.bind(self.keybind,self.event_function)
        #self.textbox.bind(self.keybind, self.event_function)
        #self.root.bind("<g>",self.event_function)
        #self.textbox.bind(self.keybind, self.event_function)
        
        self.root.mainloop()
        
        

        

    def choose_cps(self, var):
        self.cps = self.slider.get()
    

    def start_click(self):

        self.i = 1 
        while self.i == 1:
            #print("gg")
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
            time.sleep(1/self.cps)
        
    def stop_click(self):
        self.i = 2
        
    def clear(self):
        self.textbox.delete("1.0", tk.END)

    def select_bind(self):
        #self.keybind_bind = "<" + str(self.textbox.get("1.0")) + ">"
        self.keybind = str(self.textbox.get("1.0"))
        #print(self.cps)
        while True:
            if keyboard.record(until=self.keybind):
                self.event_function()
        #self.keybind = str(self.textbox.get("1.0"))

    def step(self):
        t = Thread(target = self.select_bind)
        t.daemon = True
        t.start()
        
                
        #self.textbox.bind(self.keybind_bind, self.event_function)

        #print(self.keybind)
        #print(event.char)
        #print(type(1))
        #self.keybind = self.textbox.get("1.0", tk.END):
            #print("1")
            #self.start_click()
        #pass
    def event_function(self): 
         #while True:
            #if keyboard.read_hotkey() == self.keybind:
        #if event.keysym == self.keybind and self.val == 1:
            if self.val == 1:
                self.threaded_run()
                self.val = 2
        #elif event.keysym == self.keybind and self.val == 2:
            elif self.val == 2:
                self.stop_click()
                self.val = 1
        #print(type(event.keysym))
        #print(type(self.keybind))
        #print(event.keysym)
        #print(self.keybind)

    def threaded_run(self): 
        t = Thread(target = self.start_click)
        t.daemon = True
        t.start()

    

        
AC()
    


#name = input("name: ")
#print(name)