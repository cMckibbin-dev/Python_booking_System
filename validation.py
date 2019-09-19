from tkinter import *


def EntriesNotEmpty(master):
    widgets = master.winfo_children()
    for widget in widgets:
        if type(widget) == Entry:
            if widget.get() == "":
                return False
        elif type(widget) == Frame:
            if not EntriesNotEmpty(widget):
                return False

    return True


def ValidatePhoneNumber(phoneNumber, event):
    if event == '1':
        print(len(phoneNumber))
        if not phoneNumber.isdigit():
            return False
    return True
