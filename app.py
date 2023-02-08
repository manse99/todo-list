from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('Gabriels To Do List')
root.iconbitmap('c:/gui/codemy.ico')
root.geometry("500x500")

# Define our Font

my_font = Font(
    family="courier"
    size=30
    weight="bold"
)

my_frame = Frame(root)
my_frame.pack(pady=10)

# create ListBox

my_list = Listbox(my_frame,
                  font=my_font,
                  width=25,
                  height=5,
                  bg="SystemButtonFace",
                  bd=0,
                  fg="#464646"
                  )

my_list.pack()

stuff = ["wlak", "lazy", "dog"]
# add dummy list
for item in stuff:
    my_list.insert(END, item)

root.mainloop
