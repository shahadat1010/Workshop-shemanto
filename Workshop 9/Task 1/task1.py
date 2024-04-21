"""
 Create a ProgramGUI class:

    Initialize the main window:
        Create a Tkinter main window object
         Set the title of the main window to "My Tkinter App"
         Set the size of the main window to 300x200 pixels
         Disable resizing of the main window
         Set the icon for the main window to "test.ico"
         Set the background color of the main window to light gray
         Set the cursor for the main window to a hand cursor
         Set the transparency level of the main window to 50%
         Set the main window to always stay on top of other windows
         Set the main window to be in fullscreen mode
        
     Define a method to run the main event loop:
        Start the main event loop of the main window
        
create a function to call run the program by calling the file directly:
     If yes, create an instance of the ProgramGUI class and run the main event loop

"""

import tkinter as tk

class ProgramGUI:
    def __init__(self):
        self.main = tk.Tk()  
        self.main.title("My Tkinter App")  
        self.main.geometry("300x200") 
        self.main.resizable(False, False)  
        self.main.iconbitmap("test.ico")  
        self.main.configure(bg="lightgray")  
        self.main.config(cursor="hand2")  
        self.main.attributes("-alpha", 0.5)  
        self.main.attributes("-topmost", True)  
        self.main.attributes('-fullscreen', True)

    def run(self):
        self.main.mainloop()  

if __name__ == "__main__":
    gui = ProgramGUI()
    gui.run()
