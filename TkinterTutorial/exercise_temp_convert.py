import tkinter as tk


def fahrenheit_to_celsius():
    """Convert the value for Fahrenheit to Celsius and insert the result into the corresponding lbl_result."""
    fahrenheit = ent_temperature_f.get()
    celsius = (5 / 9) * (float(fahrenheit) - 32)
    lbl_result_f['text'] = f'{round(celsius, 2)} \N{DEGREE CELSIUS}'


def celsius_to_fahrenheit():
    """Convert the value for Celsius to Fahrenheit and insert the result into the corresponding lbl_result."""
    celsius = ent_temperature_c.get()
    fahrenheit = (9 / 5) * (float(celsius)) + 32
    lbl_result_c['text'] = f'{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}'


# Set-up the window
window = tk.Tk()
window.title('Temperature Converter(tm)')
window.resizable(width=False, height=False)

# Create the Fahrenheit entry frame with an Entry widget and label in it
frm_entry_f = tk.Frame(master=window)
ent_temperature_f = tk.Entry(master=frm_entry_f, width=10)
lbl_temp_f = tk.Label(master=frm_entry_f, text="\N{DEGREE FAHRENHEIT}")
# Layout the temperature Entry and Label in frm_entry using the .grid() geometry manager
ent_temperature_f.grid(row=0, column=0, sticky="e")
lbl_temp_f.grid(row=0, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert_f = tk.Button(master=window,
                          text="\N{RIGHTWARDS BLACK ARROW}",
                          command=fahrenheit_to_celsius)
lbl_result_f = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

# Create the Celsus entry frame with an Entry widget and label in it
frm_entry_c = tk.Frame(master=window)
ent_temperature_c = tk.Entry(master=frm_entry_c, width=10)
lbl_temp_c = tk.Label(master=frm_entry_c, text="\N{DEGREE CELSIUS}")
# Layout the temperature Entry and Label in frm_entry using the .grid() geometry manager
ent_temperature_c.grid(row=1, column=0, sticky="e")
lbl_temp_c.grid(row=1, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert_c = tk.Button(master=window,
                          text="\N{RIGHTWARDS BLACK ARROW}",
                          command=celsius_to_fahrenheit)
lbl_result_c = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}")


# Set-up the layout using the .grid() geometry manager
frm_entry_f.grid(row=0, column=0, padx=10)
btn_convert_f.grid(row=0, column=1, pady=10)
lbl_result_f.grid(row=0, column=2, padx=10)


# Set-up the layout using the .grid() geometry manager
frm_entry_c.grid(row=1, column=0, padx=10)
btn_convert_c.grid(row=1, column=1, pady=10)
lbl_result_c.grid(row=1, column=2, padx=10)

# Run the application
window.mainloop()
