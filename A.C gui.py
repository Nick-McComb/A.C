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
        
        self.keybind = None
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

        self.btn1 = tk.Button(self.root, text = "1", font= ("Arial",18),bg = "#006837", command = self.choose_cps1)
        self.btn1_window = self.canvas.create_window(20,100, anchor = "n", window = self.btn1)
        self.btn2 = tk.Button(self.root, text = "2", font= ("Arial",18), bg = "#1A9850", command = self.choose_cps2)
        self.btn2_window = self.canvas.create_window(60,100, anchor = "n", window = self.btn2)
        self.btn3 = tk.Button(self.root, text = "3", font= ("Arial",18),bg = "#66BD63", command = self.choose_cps3)
        self.btn3_window = self.canvas.create_window(100,100, anchor = "n", window = self.btn3)
        self.btn4 = tk.Button(self.root, text = "4", font= ("Arial",18),bg = "#A6D96A", command = self.choose_cps4)
        self.btn4_window = self.canvas.create_window(140,100, anchor = "n", window = self.btn4)
        self.btn5 = tk.Button(self.root, text = "5", font= ("Arial",18), bg = "#D9EF8B", command = self.choose_cps5)
        self.btn5_window = self.canvas.create_window(180,100, anchor = "n", window = self.btn5)
        self.btn6 = tk.Button(self.root, text = "6", font= ("Arial",18), bg = "#FEE08B", command = self.choose_cps6)
        self.btn6_window = self.canvas.create_window(220,100, anchor = "n", window = self.btn6)
        self.btn7 = tk.Button(self.root, text = "7", font= ("Arial",18),bg = "#FDAE61", command = self.choose_cps7)
        self.btn7_window = self.canvas.create_window(260,100, anchor = "n", window = self.btn7)
        self.btn8 = tk.Button(self.root, text = "8", font= ("Arial",18), bg = "#F46D43", command = self.choose_cps8)
        self.btn8_window = self.canvas.create_window(300,100, anchor = "n", window = self.btn8)
        self.btn9 = tk.Button(self.root, text = "9", font= ("Arial",18),bg = "#D73027", command = self.choose_cps9)
        self.btn9_window = self.canvas.create_window(340,100, anchor = "n", window = self.btn9)
        self.btn10 = tk.Button(self.root, text = "10", font= ("Arial",18), height= 1, width = 2,bg = "#A50026", command = self.choose_cps10)
        self.btn10_window = self.canvas.create_window(380,100, anchor = "n", window = self.btn10)
        

        self.select_btn = tk.Button(self.root, text= "Select",font =("Arial",18), command = self.select_bind) #command = lambda:[self.start_click, self.stop_btn])
        self.select_btn_window = self.canvas.create_window(200,200, anchor= "n", window = self.select_btn)
        #self.select_btn.bind("<KeyPress>",self.start_short)
        self.clear_btn = tk.Button(self.root, text = "Clear", font = ("Arial",12), height=1 , width= 4, command= self.clear)
        self.clear_btn_window = self.canvas.create_window(240, 157, anchor = "n", window = self.clear_btn)

        self.stop_btn = tk.Button(self.root, text ="Stop", font = ("Arial", 18), command = self.stop_click)
        self.stop_btn_window = self.canvas.create_window(200, 250, anchor= "n", window = self.stop_btn)
        #self.stop_btn.bind("<KeyPress>",self.stop_short)

        self.textbox = tk.Text(self.root, height= 1, width= 1, font = ("Arial", 16))
        self.textbox_window = self.canvas.create_window(200,160, anchor = "n", window = self.textbox)
        self.textbox.bind("<KeyPress>",self.event_function)

        self.root.mainloop()

    def choose_cps1(self):
        self.cps = 1
    def choose_cps2(self):
        self.cps = 2
    def choose_cps3(self):
        self.cps = 3
    def choose_cps4(self):
        self.cps = 4
    def choose_cps5(self):
        self.cps = 5
    def choose_cps6(self):
        self.cps = 6
    def choose_cps7(self):
        self.cps = 7
    def choose_cps8(self):
        self.cps = 8
    def choose_cps9(self):
        self.cps = 9
    def choose_cps10(self):
        self.cps = 10

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
        self.keybind = str(self.textbox.get("1.0"))
        #print(self.keybind)
        #print(event.char)
        #print(type(1))
        #self.keybind = self.textbox.get("1.0", tk.END):
            #print("1")
            #self.start_click()
        #pass
    def event_function(self, event): 

        if event.keysym == self.keybind and self.val == 1:
            self.threaded_run()
            self.val = 2
        elif event.keysym == self.keybind and self.val == 2:
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