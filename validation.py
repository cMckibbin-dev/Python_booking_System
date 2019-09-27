from tkinter import *
from tkinter import ttk
import re
from gui import dialogs


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
        if not char_limit(string, 100):
            return False
    return True


def noSpecialCharacter(value, string, event):
    if event == '1':
        regex = re.compile('[@_!#$%^&*()<>?/|}{~:"]')
        if regex.match(value):
            return False
        if not char_limit(string, 100):
            return False
    return True


def ValidatePhoneNumber(value, string,  event):
    if event == '1':
        regex = re.compile('[+]')
        if not value.isdigit() and not regex.match(value):
            return False
        if not char_limit(string, 25):
            return False
    return True


def char_limit(value, limit):
    print(value)
    print(len(value))
    if len(value) > limit:
        dialogs.limit_reached(limit)
        return False
    return True
