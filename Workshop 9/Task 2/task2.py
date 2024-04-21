"""
Create a SandwichOrderApp class:

  Initialize the main window:
        Set the title of the window to "Sandwich Order"
        Create labels, radio buttons for bread selection, checkboxes for fillings and extras, and a Submit Order button
        Set the default bread selection to "White"
        Define a function to handle order submission when the Submit Order button is clicked
        Start the main event loop to display the GUI
    
  Define a function to handle order submission:
        Retrieve the selected bread type
        Retrieve the selected fillings and extras
        If no fillings are selected, display an error message
        If fillings are selected, construct the order details message
        Display the order details message in a pop-up window
"""


import tkinter as tk

class ImageToggleApp:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title("Image Toggle")

        # Create PhotoImage objects for two images
        self.image1 = tk.PhotoImage(file='image1.png')
        self.image2 = tk.PhotoImage(file='image2.png')

        # Create a Label widget to display the initial image
        self.image_label = tk.Label(self.main_window, image=self.image1)

        # Create a Button widget to toggle between images
        self.toggle_button = tk.Button(self.main_window, text="Toggle Image", command=self.toggle_image)

        # Pack the widgets into the main window
        self.image_label.pack()
        self.toggle_button.pack()

        # Start the main event loop
        self.main_window.mainloop()

    def toggle_image(self):
        current_image = self.image_label.cget("image")
        if current_image == str(self.image1):
            self.image_label.configure(image=self.image2)
        else:
            self.image_label.configure(image=self.image1)

# Create an instance of the ImageToggleApp class
app = ImageToggleApp()
