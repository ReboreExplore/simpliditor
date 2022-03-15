import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

   
def Setup():
    window = tk.Tk() # create a window
    window.title("myneweditor")

    window.rowconfigure(0,minsize=900,weight=1)
    window.columnconfigure(1, minsize=900,weight=1)

    txt_edit = tk.Text(window)
    fr_buttons = tk.Frame(window,relief=tk.RAISED, bd=2)

    f1 = File_Ops(txt_edit,window)
    functions = [f1.open_file,f1.new_file,f1.save_file] # add the new functionalities
    features = ['Open','New','Save As']
    c1 = Container_Config(fr_buttons,txt_edit)
    c1.config_window()
    for i,btn in enumerate(features):
        c1.button_config(btn,functions[i],i)
    
    window.mainloop()

class Container_Config:
    def __init__(self,fr_buttons,txt_edit):
        self.fr_buttons = fr_buttons
        self.txt_edit = txt_edit

    def button_config(self,box_text,function,i):
        btn = tk.Button(self.fr_buttons,text = box_text,command = function)
        btn.grid(row = i,column=0, sticky="ew", padx=5, pady=5)

    def config_window(self):
        self.fr_buttons.grid(row=0, column=0, sticky="ns") # ns is for letting this container expand vertically
        self.txt_edit.grid(row=0, column=1, sticky="nsew") # nsew is to allow this grid cell to expand in all direction

class File_Ops:
    def __init__(self,txt_edit,window):
        self.txt_edit = txt_edit
        self.window = window

    def open_file(self):
        """Open a file for editing."""
        filepath = askopenfilename(filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        # if clicks Cancel
        if not filepath:
            return self.txt_edit.delete(1.0, tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            self.txt_edit.insert(tk.END, text)
        self.window.title(f"myneweditor - {filepath}")
    
    def new_file(self):
        """ Create a new file """
        global file_name
        file_name = 'untitled.txt'
        self.txt_edit.delete('1.0',tk.END)
        self.window.title(file_name)

    def save_file(self):
        """Save the current file as a new file."""
        filepath = asksaveasfilename(defaultextension="txt",filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],)
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = self.txt_edit.get(1.0, tk.END)
            output_file.write(text)
        self.window.title(f"myneweditor - {filepath}")


if __name__=='__main__':
    Setup()
    



