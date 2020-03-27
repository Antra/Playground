import tkinter as tk

window = tk.Tk()


# Capture key press and send to STDOUT
def handle_keypress(event):
    """Print the character associated to the key pressed"""
    print(event.char)


# Bind keypress event to handle_keypress()
window.bind("<Key>", handle_keypress)


# Capture button click and send to STDOUT
def handle_click(event):
    print('The button was clicked!')


button = tk.Button(text='Click me!')
button.pack()

# Bind left mouse button events on the button widget to handle_click()
button.bind("<Button-1>", handle_click)

window.mainloop()
