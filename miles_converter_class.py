#  CS 3B Intermediate Software Design in Python
#  Lab # 6
#  Module: GUI
#  Description: This class creates a GUI that converts kilometers to miles
#  Development Env:  Windows 10
#  Version:  Python 3.11
#  Module filename:  aldosiswantoLab6.py
#  Date:  3/15/23
#

# Import classes
import tkinter as tk
from tkinter.messagebox import showinfo


class App:
    # Constants
    APP_TITLE = 'Kilometers to Miles Converter'
    APP_SIZE = "350x50"

    """
    Initializes the App Frame
    """

    def __init__(self):
        root = tk.Tk()
        root.title(App.APP_TITLE)
        root.geometry(App.APP_SIZE)
        distanceConverter(root).pack(side='top')
        root.mainloop()


class distanceConverter(tk.Frame):
    """
    Initializes the distance converter objects
    @param parent: the parent frame
    """

    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent
        self.label = self.create_text_entry_label()
        self.entry_box = self.create_text_entry_box()
        self.convert_button = self.create_convert_button()
        self.quit_button = self.create_quit_button()

        self.label.grid(row=1, column=1, columnspan=2)
        self.entry_box.grid(row=1, column=3, columnspan=2)
        self.convert_button.grid(row=2, column=2)
        self.quit_button.grid(row=2, column=3)

    """
    Create the text entry label
    @return label: the label object containing user prompt
    """

    def create_text_entry_label(self):
        label = tk.Label(self, text='Enter distance (Miles): ')
        return label

    """
    Creates the text entry box
    @return entry_box: the entry box object to insert data
    """

    def create_text_entry_box(self):
        entry_box = tk.Entry(self)
        return entry_box

    """
    Creates the convert button
    @return convert_button: the convert button to convert to miles
    """

    def create_convert_button(self):
        convert_button = tk.Button(self, text='Convert', command=self.convert)
        return convert_button

    """
    Creates the quit button
    @return quit_button: the quit button to close the program
    """

    def create_quit_button(self):
        quit_button = tk.Button(self, text='Quit', command=self.quit_program)
        return quit_button

    """
    Convert event to convert km to miles
    """

    def convert(self):
        cnvrt_obj = KilometersToMiles(self.entry_box.get())

        if cnvrt_obj.success:
            showinfo('Converted to Miles!',
                     '{:.2f}km is equivalent to {:.2f}miles'.format(
                         cnvrt_obj.km,
                         cnvrt_obj.miles
                         ))
        self.entry_box.delete(0, 'end')

    """
    Quit the program
    """

    def quit_program(self):
        self.parent.destroy()


class KilometersToMiles:
    # Constants
    KM_TO_MILES_MULTIPLIER = 0.621371

    """
    Initializes a class to store miles values from the user
    @param km: the km values inserted by the user
    """

    def __init__(self, km):
        self.success = True
        self.__value = None

        self.km = km

    """
    Getter function for miles
    @return miles: the values in miles
    """

    @property
    def miles(self):
        return KilometersToMiles.KM_TO_MILES_MULTIPLIER * self.km

    """
    Getter function for km
    @return km: the values in kilometers
    """

    @property
    def km(self):
        return self.__km

    """
    Setter function for km
    @param km: the kilometer value input from user
    """

    @km.setter
    def km(self, km):
        try:
            self.__km = float(km)
        except Exception as e:
            showinfo('ERROR', 'Input is not a string. Please try again. \n\n'
                     + str(e))
            self.success = False
