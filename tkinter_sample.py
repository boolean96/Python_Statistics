import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext
from tkinter import ttk

global selection
selection=""

def import_csv():
    filename = askopenfilename()
    text_area.insert(tk.INSERT,"CSV Imported : "+filename)
    text_area.update_idletasks()

def mean():
    text_area.insert(tk.INSERT,"Mean Running")

def median():
    text_area.insert(tk.INSERT,"Median Running")

def range():
    text_area.insert(tk.INSERT,"Range Running")

def select(eventObject):
    selection = eventObject.widget.get()
    print(selection)

def calc_selection():
    #selection = comboExample.get()
    #print(selection)
    print("Test")

root = tk.Tk()
root.title("Welcome to the Statistics Python App")
label = tk.Label(root, fg="dark green")

comboExample = ttk.Combobox(root, values=["Mean","Medium","Range"])
comboExample.pack(side="bottom")
#comboExample.current(1)
comboExample.bind("<<ComboboxSelected>>", select)

calculate_button = tk.Button(root, text='Calculate!', foreground='green', width=25, command=calc_selection())
calculate_button.pack(side="bottom") 

#print(comboExample.current(), comboExample.get())

text_area = scrolledtext.ScrolledText(root,  wrap = tk.WORD,width=40,height=10,background="white",foreground="black",font=("Times New Roman",15)) 
text_area.pack(side="bottom")  

button = tk.Button(root, text='Close Program', foreground='red', width=8, command=root.destroy)
button.pack()

button_csv = tk.Button(root, text='Import CSV Data', foreground='blue', width=25, command=import_csv)
button_csv.pack(side="bottom") 

root.mainloop()