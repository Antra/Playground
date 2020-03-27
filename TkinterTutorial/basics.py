import tkinter as tk

window = tk.Tk()
frame = tk.Frame()
frame.pack()

# Colourchart of the possible Tkinter colours: http://www.science.smith.edu/dftwiki/index.php/File:TkInterColorCharts.png
# Width and height are measured in "text units", based on the width and height of the character '0'.
label = tk.Label(text='Python rocks!',
                 foreground="white",
                 background="black",
                 width=10,
                 height=10,
                 master=frame)
label.pack()

# A button is basically a clickable label - albeit one that can execute functions on click
button = tk.Button(text='Click me!',
                   fg="yellow",
                   bg="blue",
                   width=25,
                   height=5)
button.pack()

entry = tk.Entry(fg='yellow',
                 bg='blue',
                 width=50)
entry.pack()

text_box = tk.Text()
text_box.pack()

window.mainloop()
