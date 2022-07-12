import tkinter as tk

class Application(tk.Tk):
     def __init__(self):
        tk.Tk.__init__(self)
        self.geometry('500x500')
        self.title('Your first App')
        
        first_label = tk.Label(self, text = "I'm a cool App!!", font=10)
        first_label.pack(padx = 3, pady = 3)
        first_button = tk.Button(self, text ="Hello World", command = hello)
        first_button.pack(padx= 5, pady = 5)
        Application.first_entry = tk.Entry(self, width = 30)
        Application.first_entry.pack(padx = 7, pady = 7)

def hello():
    x = Application.first_entry.get()
    print(x)
app = Application()
app.mainloop()