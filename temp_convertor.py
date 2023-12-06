"""
Please click '?' button inside program for a complete manual/credits
"""

# importing tkinter, naming it something easy to write
import tkinter as tk
from random import randint

# Reading .txt file that contains help.txt, this is converted into python strings for display
manual = open('help.txt', 'r')
manual_text = manual.read()
manual.close()

# Determines what type of conversion is going on
is_fahren = True


def initializer():
    if is_fahren:  # if we are converting from fahrenheit, show the user
        btn_switch['text'] = '\N{DEGREE FAHRENHEIT}'

    else:  # if we are converting from celsius, show the user
        btn_switch['text'] = '\N{DEGREE CELSIUS}'

    convert()  # update the results, makes calculator more polished


def convert():
    try:

        if ent_temp.get() == "random":
            # shh, don't tell anyone about this
            # check the value of ent_temp, if it equals the string 'random' generate a random temperature
            temp = randint(0, 100)  # generate random temperature between 0 and 100
            ent_temp.delete(0, tk.END)  # delete string random
            ent_temp.insert(0, temp)  # replace ent_temp with random temperature

        else:
            temp = float(ent_temp.get())  # if the user actually has real data to enter this skips all the other stuff

        if is_fahren:  # check program state
            # do math
            temp = (temp - 32) * 5 / 9

            # post result
            lbl_result['text'] = f'{temp: 0.2f} \N{DEGREE CELSIUS}'

        if not is_fahren:  # same thing as last module but for celsius
            temp = (9 / 5) * temp + 32

            lbl_result['text'] = f'{temp: 0.2f} \N{DEGREE FAHRENHEIT}'

    except ValueError:
        # if the value entered is non numerical this throws an error message, also gets rid of error
        # printing to terminal
        lbl_result['text'] = 'ERROR: Not numeric'


def switch_mode():
    global is_fahren  # get the global is_fahren variable, it only let me update if i used global when calling it
    is_fahren = not is_fahren  # inverse is_fahren
    initializer()  # update buttons and labels


def spawn_window():
    man_window = tk.Tk()  # spawn window
    man_window.title("User Manual")  # name window
    man_window.resizable(width=False, height=False)  # set unresizeable

    text_box = tk.Text(master=man_window, height=30, width=100)  # instantiate text box

    text_box.insert("1.0", manual_text)  # add manual text

    text_box.pack()  # send to window
    text_box.config(state='disabled')  # make uneditable

    man_window.mainloop()  # run window loop


# Create window
window = tk.Tk()
window.title("Temperature Convertor")
window.resizable(width=False, height=False)

# Generate Frame
frm_entry = tk.Frame(master=window)

# Instantiate all buttons, labels, and entry boxes
ent_temp = tk.Entry(
    master=frm_entry,
    width=10)

lbl_result = tk.Label(
    master=frm_entry,
    relief=tk.SUNKEN,
    text='0 \N{DEGREE CELSIUS}',
    width=20)

btn_convert = tk.Button(
    master=frm_entry,
    relief=tk.RIDGE,
    text='\N{RIGHTWARDS BLACK ARROW}',
    command=convert)

btn_switch = tk.Button(
    master=frm_entry,
    relief=tk.RIDGE,
    text='\N{DEGREE FAHRENHEIT}',
    command=switch_mode)

btn_help = tk.Button(
    master=frm_entry,
    relief=tk.RIDGE,
    text='?',
    font='Helvetica 10 bold',
    command=spawn_window)

# Display all elements to the screen
frm_entry.pack()
ent_temp.grid(row=0, column=0, sticky='e', padx=10)
lbl_result.grid(row=0, column=3, sticky='nsew', padx=10)
btn_convert.grid(row=0, column=2, sticky='nsew', padx=2)
btn_switch.grid(row=0, column=1, sticky='nsew', padx=2)
btn_help.grid(row=0, column=4, sticky='nsew', padx=2)

# Set up the calculator for users
ent_temp.insert(0, '32')
initializer()

# Calls mainloop and runs program
window.mainloop()
