# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor is tested to run in recent versions of
# Chrome, Firefox, Safari, and Edge.

# import simplegui  # simplegui is for CodeSkulptor only

import tkinter as tk  # Replacement for local Python

message = "Welcome!"

# Handler for mouse click
def click():
    global message
    message = "Good job!"
    label.config(text=message)

# Handler to draw on canvas (not needed in tkinter, handled by label)

# --- Replacement for simplegui frame setup ---
root = tk.Tk()
root.title("Home")
root.geometry("1020x800")

label = tk.Label(root, text=message, font=("Arial", 24), fg="red")
label.pack(pady=40)

button = tk.Button(root, text="Click me", command=click)
button.pack()

root.mainloop()