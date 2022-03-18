import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askopenfilename, asksaveasfilename
 

def create_frame_config(window):
    file_buttons = ttk.Frame(window)
    edit_buttons = ttk.Frame(window)
    txt_editor = tk.Text(window)
    
    idx_file = [1,0]
    text_config(txt_editor)
    
    #  Get the file functionalities
    f1 = File_Ops(txt_editor,window)
    functions = [f1.open_file,f1.new_file,f1.save_file]
    features = ['Open','New','Save As']

    # Configure the buttons
    c1=Button_Config(file_buttons)
    c1.config_window(idx_file)
    for i,btn in enumerate(features):
        c1.button_config(btn,functions[i],i,0) # row change and column 0

    idx_edit = [0,1]
    # Get the functionalities
    edits = ['Copy','Paste','Cut']

    # Configure the buttons
    c2 = Button_Config(edit_buttons)
    c2.config_window(idx_edit)
    for i,btn in enumerate(edits):
        c2.button_config(btn,edits[i],0,i) # row change and column 0

def text_config(txt_editor):
    txt_editor.grid(row=1, column=1, sticky="nsew")

class Button_Config:
    def __init__(self,buttons):
        self.buttons = buttons

    def button_config(self,box_text,function,i,j):
        btn = tk.Button(self.buttons,text = box_text,command = function)
        btn.grid(row = i,column=j, sticky="ew", padx=5, pady=5)

    def config_window(self,idx):
        self.buttons.grid(row=idx[0], column=idx[1], sticky="ns") # ns is for letting this container expand vertically

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
        self.txt_edit.delete('1.0',tk.END) #'1.0' means line 1 character 0
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

class App_setup(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simpliditor") # add a title to the window
        self.geometry('1000x1000+50+50') # set the window size
        self.attributes('-alpha',0.3) # make transparent window
        self.resizable(0, 0)
        #self.iconbitmap('./assets/simpliditor_icon.ico') # set custom icon

        self.rowconfigure(0,weight=1)
        self.rowconfigure(1,weight=12)
        self.columnconfigure(0,weight=1)
        self.columnconfigure(1,weight=12)

        self.__create_widgets()
    
    def __create_widgets(self):
        frame = create_frame_config(self) # calls the mainloop method of the tk.Tk class which freezes the program until close it


if __name__=='__main__':
    text_app = App_setup()
    text_app.mainloop()
    



