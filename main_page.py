import tkinter as tk
import csv
from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext
from tkinter import ttk

class MainApplication(tk.Frame):
    def __init__(self, master):
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.create_widgets()
        self.configure_gui()

    def show_output(self,message):
        self.text_area.config(state=tk.NORMAL)
        if message == 'CLEAR':
            self.text_area.delete(1.0,tk.END)
        else:
            self.text_area.insert(tk.INSERT,message)
            self.text_area.update_idletasks()
        self.text_area.config(state=tk.DISABLED)

    def calc_selection(self):
        selection = self.comboExample.get()

    def output_clear(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0,tk.END)
        self.text_area.config(state=tk.DISABLED)
    
    def import_csv(self):
        filename = askopenfilename()
        self.show_output("CSV Imported : "+filename)
        with open(filename, newline='') as csvfile:
            data = list(csv.reader(csvfile))
            for value in data:
                #self.text_area.insert(tk.INSERT,value)
                for val in value:
                    self.text_area.config(state=tk.NORMAL)
                    self.text_area.insert(tk.INSERT,val)
                    self.text_area.config(state=tk.DISABLED)

    def configure_gui(self):
       #ComboBox
        self.comboExample.pack(side="bottom")
        #Calculate Button
        self.calculate_button.pack(side="bottom")
        #Clear Output Button
        self.clear_button.pack(side="bottom")
        #Output Box
        self.text_area.pack(side="bottom")
        #Close Button
        self.button.pack()
        #CSV Import Button
        self.button_csv.pack(side="bottom") 

    def create_widgets(self):
        #ComboBox
        self.comboExample = ttk.Combobox(root, values=["Mean","Medium","Range"])
        #Calculate Button
        self.calculate_button = tk.Button(root, text='Calculate!', foreground='green', width=25, command=self.calc_selection)
        #Clear Output Button
        self.clear_button = tk.Button(root, text='Clear!', foreground='red', width=25, command=self.output_clear)
        #Output Box
        self.text_area = scrolledtext.ScrolledText(root,  wrap = tk.WORD,width=40,height=10,background="white",foreground="black",font=("Times New Roman",15))
        self.text_area.config(state=tk.DISABLED)
        #Close Button
        self.button = tk.Button(root, text='Close Program', foreground='red', width=8, command=root.destroy)
        #CSV Import Button
        self.button_csv = tk.Button(root, text='Import CSV Data', foreground='blue', width=25, command=self.import_csv) 

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Welcome to the Statistics Python App")
    main_app =  MainApplication(root)
    root.mainloop()
            