from tkinter import *
from tkinter import ttk
import re


def EntriesNotEmpty(master):
    """function will return True if all entry widgets in an given root are not empty"""
    widgets = master.winfo_children()
    for widget in widgets:
        if type(widget) == Entry or type(widget) == ttk.Combobox:
            if widget.get() == "":
                return False
        elif type(widget) == Frame:
            if not EntriesNotEmpty(widget):
                return False
    return True





def NumbersOnly(value, event):
    """Function will return True if value is a digit"""
    if event == '1':
        if not value.isdigit():
            return False
    return True


def lettersOnly(char, event):
    """function will return true if value is a letter"""
    if event == '1':
        if not char.isalpha() and not char.isspace():
            return False
    return True


def noSpecialCharacter(value, event):
    if event == '1':
        regex = re.compile('[@_!#$%^&*()<>?/|}{~:"]')
        if regex.match(value):
            return False
    return True


def ValidatePhoneNumber(phoneNumber, event):
    if event == '1':
        print(len(phoneNumber))
        if not phoneNumber.isdigit():
            return False
    return True
