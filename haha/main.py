import tkinter as tk

# Create the main window

root = tk.Tk()

root.title("Simple Tkinter Example")

# Create a label

label = tk.Label(root, text="Hello, Tkinter!", font=("Helvetica", 16))

label.pack(pady=10)

# Create a button

button = tk.Button(root, text="Click Me!", font=("Helvetica", 14), command=lambda: label.config(text="Button Clicked!"))

button.pack(pady=10)

# Run the application

root.mainloop()