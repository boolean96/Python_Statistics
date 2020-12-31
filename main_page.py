import tkinter as tk
import csv
import statistics as sts
from tkinter.filedialog import askopenfilename
from tkinter import scrolledtext
from tkinter import ttk

class MainApplication(tk.Frame):
    
    data_list = []
    def __init__(self, master):      
        self.master = master
        tk.Frame.__init__(self, self.master)
        self.create_menubar()
        self.create_widgets()
        self.configure_gui()

    def create_menubar(self):
        #Menu Bar
        self.menubar = tk.Menu(root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.menubar.add_cascade(label = "Models", menu = self.filemenu)
        self.filemenu.add_command(label="Multiple Regression", command=self.multiple_regression)
        root.config(menu = self.menubar)

    def show_output(self,message):
        self.text_area.config(state=tk.NORMAL)
        if message == "CLEAR":
            self.text_area.delete(1.0,tk.END)
        else:
            self.text_area.insert(tk.INSERT,message)
            self.text_area.update_idletasks()
        self.text_area.config(state=tk.DISABLED)
    
    def multiple_regression(self):
        self.show_output("CLEAR")
        self.show_output("Run Multiple Regression Model")
        #self.root.withdraw()
        t = tk.Toplevel(self)
        t.wm_title("Multiple Regression")
        l = tk.Label(t, text="Run Multiple Regression Model")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=100)
        print("Run Multiple Regression Model")

    def calc_selection(self):
        selection = self.comboExample.get()
        if selection == "Mean":
            self.show_output("CLEAR")
            self.show_output(sts.mean(self.data_list))
        if selection == "Median":
            self.show_output("CLEAR")
            self.show_output(sts.median(self.data_list))
        if selection == "Mode":
            self.show_output("CLEAR")
            self.show_output(sts.mode(self.data_list))
        if selection == "Range":
            self.show_output("CLEAR")
            self.show_output((max(self.data_list)) - (min(self.data_list)))
        if selection == "Sample Standard Deviation":
            self.show_output("CLEAR")
            self.show_output(sts.stdev(self.data_list))
        if selection == "Sample Variance":
            self.show_output("CLEAR")
            self.show_output(sts.variance(self.data_list))
        if selection == "Population Standard Deviation":
            self.show_output("CLEAR")
            self.show_output(sts.pstdev(self.data_list))
        if selection == "Population Variance":
            self.show_output("CLEAR")
            self.show_output(sts.pvariance(self.data_list))
        

    def output_clear(self):
        self.show_output("CLEAR")
    
    def import_csv(self):
        self.data_list.clear()
        filename = askopenfilename()
        self.show_output("CSV Imported : "+filename)
        with open(filename, newline='') as csvfile:
            data = list(csv.reader(csvfile))
            for value in data:
                for val in value:
                    self.data_list.append(float(val))

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
        self.comboExample = ttk.Combobox(root, values=["Mean",
                                                       "Median",
                                                       "Mode",
                                                       "Range",
                                                       "Sample Standard Deviation",
                                                       "Sample Variance",
                                                       "Population Standard Deviation",
                                                       "Population Variance"
                                                       ])
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
            