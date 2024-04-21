"""
Create a SandwichOrderApp class:

     Initialize the main window
        Set the title of the window
        Create labels, radio buttons, checkboxes, and a submit button
        Define variables to store bread selection and filling/extras choices
        Bind the submit button to a function to handle order submission
        Start the main event loop
    
    Define a function to handle order submission:
        Retrieve the selected bread type
        etermine the selected fillings and extras
        If no fillings are selected, display an error message
        If fillings are selected, construct and display the order details

"""

import tkinter as tk
from tkinter import messagebox

class SandwichOrderApp:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Sandwich Order")
        tk.Label(self.main_window, text="Choose your bread:").grid(row=0, column=0, sticky=tk.W)
        self.bread_var = tk.StringVar()
        self.bread_var.set("White")
        tk.Radiobutton(self.main_window, text="White", variable=self.bread_var, value="White").grid(row=0, column=1, sticky=tk.W)
        tk.Radiobutton(self.main_window, text="Wholemeal", variable=self.bread_var, value="Wholemeal").grid(row=0, column=2, sticky=tk.W)

        tk.Label(self.main_window, text="Choose your fillings:").grid(row=1, column=0, sticky=tk.W)
        self.cb1_var = tk.IntVar()
        self.cb2_var = tk.IntVar()
        self.cb3_var = tk.IntVar()
        self.cb1 = tk.Checkbutton(self.main_window, text="Ham", variable=self.cb1_var)
        self.cb1.grid(row=1, column=1, sticky=tk.W)
        self.cb2 = tk.Checkbutton(self.main_window, text="Cheese", variable=self.cb2_var)
        self.cb2.grid(row=1, column=2, sticky=tk.W)
        self.cb3 = tk.Checkbutton(self.main_window, text="Tomato", variable=self.cb3_var)
        self.cb3.grid(row=1, column=3, sticky=tk.W)

        tk.Label(self.main_window, text="Choose your extras:").grid(row=2, column=0, sticky=tk.W)
        self.cb4_var = tk.IntVar()
        self.cb5_var = tk.IntVar()
        self.cb6_var = tk.IntVar()
        self.cb4 = tk.Checkbutton(self.main_window, text="Lettuce", variable=self.cb4_var)
        self.cb4.grid(row=2, column=1, sticky=tk.W)
        self.cb5 = tk.Checkbutton(self.main_window, text="Mayonnaise", variable=self.cb5_var)
        self.cb5.grid(row=2, column=2, sticky=tk.W)
        self.cb6 = tk.Checkbutton(self.main_window, text="Mustard", variable=self.cb6_var)
        self.cb6.grid(row=2, column=3, sticky=tk.W)

        self.submit_button = tk.Button(self.main_window, text="Submit Order", command=self.submit_order)
        self.submit_button.grid(row=3, column=0, columnspan=4)
        self.main_window.mainloop()

    def submit_order(self):
        bread = self.bread_var.get()
        fillings = [self.cb1_var.get(), self.cb2_var.get(), self.cb3_var.get()]
        selected_fillings = [filling for filling in ["Ham", "Cheese", "Tomato"] if fillings.pop(0)]
        if not selected_fillings:
            messagebox.showerror("Error", "Please select at least one filling.")
        else:
            fillings_text = ", ".join(selected_fillings)
            extras = [self.cb4_var.get(), self.cb5_var.get(), self.cb6_var.get()]
            extras_text = ", ".join([extra for extra in ["Lettuce", "Mayonnaise", "Mustard"] if extras.pop(0)])
            order_details = f"Bread: {bread}\nFillings: {fillings_text}\nExtras: {extras_text}"
            messagebox.showinfo("Order Details", order_details)


app = SandwichOrderApp()
