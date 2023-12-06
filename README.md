# Temperature-Calculator
This program is a python temperature convertor that uses TKinter to display a GUI. First time messing around with TKinter

Thank you for using the Temperature Calculator!

Author: Charlie Shaneck
Date: 12/6/23
Version: 2.1

How to use:

- The program has 4 main features

1 - A box to enter temperatures
2 - A button to change between Celsius and Fahrenheit (Kelvin functionality coming soon!)
3 - A button to convert the entered temperature
4 - A box to display the result
- the program also has a button to bring up this guide

To use the calculator:
Click the degrees symbol until it matches the temperature you wish to convert from
Enter the temperature you would like to convert from
Click the arrow button
!*! Behold the calculator in all its glory !*!


This calculator is open source!
Feel free to edit it however you want,
below is a short docs to make editing easier, code has also been commented for ease of use

Imports and Setups:
    tk - Standard Library Module, tkinter, has been imported as tk for ease of use
    manual - (.txt file) This opens this file to read the user manual
    manual_text - (str) Stores manual as a string for printing to display
    is_fahren - (bool) Stores whether this is a C -> F calcualtor or a F -> C calculator

Functions:
    initializer()
        Detects what state is_fahren is in and changes the switch mode button to reflect this and show the user
        calls convert() to update the result and make the calculator more polished

    convert()
        Converts between temperatures. Contains main functionality of program
        checks is_fahren to see what state the calcualtor is in
        converts temp to reflect this
        updates the result label to show results

        Variables:
            temp - (float) stores the temperature value

    switch mode()
        changes is_fahren to its opposite
        calls initializer to update labels and buttons

    spawn_window()
        Creates help window, is called when the '?' button is clicked
        variables:
            man_window - (Tk) a blank window class from tkinter
                initialized to be unresizable and named "User Manual"

            text_box - (tk.Text) a text box, uneditable and written in with this file

    Variables:
        Window - (Tk) main window for the program
        frm_entry - (Frame) The frame that contains the buttons and labels
        ent_temp - (Entry) the box to enter the temperature
        lbl_result - (Label) The box that contains the results
        btn_convert - (Button) When clicked it converts the entered temperature
        btn_switch - (Button) When clicked it switches calculator mode
        btn_help - (Button) when clicked it opens the help window


Changelog:
Version 1.0:
- Added celsius to fahrenheit conversion
- Created basic functionality

Version 1.1
- Added fahrenheit to celsius conversion
- Updated code, added input checkers

Version 2.0
- Complete rewrite of the code base
- Added GUI

Version 2.1
- Polished GUI
- Added this manual page
