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
        for v in value:
            if not v.isdigit():
                return False
    return True


def lettersOnly(char, string, event):
    """function will return true if value is a letter"""
    if event == '1':
        for c in char:
            if not c.isalpha() and not c.isspace():
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
