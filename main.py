from tkinter import *
import tkinter.font as tkFont
import datetime, threading


root = Tk() # Tkinter root
root.title("Live Clock") #Tkinter title
root.geometry('900x500')

try:
    root.iconbitmap("icon.ico") # Icon
except:
    pass

class App():
    def __init__(self):
        self.root = root

        # List of things to eliminate
        self.delete = []
        #main page
        self.frame = self.create_frame(self.root)
        self.frame.pack()
        self.now = ""


        threading.Thread(target=lambda: self.Main_Page()).start()
        self.root.mainloop()

    
    # Create a Frame Function
    def create_frame(self, root):
        return Frame(root, highlightthickness=0, borderwidth=0)

    # Add a Object to the list of things to Delete
    def add(self, data):
        return self.everything.append(data)

    # Delete all the things in question
    def Delete(self):
        try:
            for a in self.everything:
                a.destroy()
        except NameError:
            pass
    
    # Main Page
    def Main_Page(self):

        day_font = tkFont.Font(family="Segoe UI Black", size=50)
        day = Label(self.frame, text="", font=day_font, fg="#383838", padx=20)
        day.pack()
        hour_font = tkFont.Font(family="Segoe UI Black", size=30)
        hour = Label(self.frame, text="", font=hour_font, fg="#383838", padx=20, pady=20)
        hour.pack()

        while True:
            self.now = datetime.datetime.now()
            day.config(text = f"{self.now.day:02d}/{self.now.month:02d}/{self.now.year:02d}")
            hour.config(text = f"{self.now.hour:02d}:{self.now.minute:02d}:{self.now.second:02d}")



if __name__ == '__main__':
    app = App()
    app(root)
