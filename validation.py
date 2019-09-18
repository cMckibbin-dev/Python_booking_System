from tkinter import *


def EntriesNotEmpty(master):
    widgets = master.winfo_children()
    notEmpty = True
    for widget in widgets:
        if type(widget) == Entry:
            if widget.get() == "":
                return False
        elif type(widget) == Frame:
            notEmpty = EntriesNotEmpty(widget)

    return True if notEmpty else False


def ValidatePhoneNumber(phoneNumber, event):
    if event == '1':
        print(phoneNumber)
        if not phoneNumber.isdigit() and not len(phoneNumber) <= 11:
            return False
    return True
