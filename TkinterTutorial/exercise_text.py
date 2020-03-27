import tkinter as tk

window = tk.Tk()

ent_text = tk.Entry(width=40,
                    fg='black',
                    bg='white')
ent_text.pack()

ent_text.insert('0', 'What is your name?')

window.mainloop()
