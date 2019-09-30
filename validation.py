from tkinter import *
from tkinter import ttk
import re
from gui import dialogs


def EntriesNotEmpty(master):
    """function will return True if all entry widgets in an given root are not empty"""
    widgets = master.winfo_children()
    for widget in widgets:
        if type(widget) == Entry or type(widget) == ttk.Combobox:
            if widget.get() == "" or widget.get().isspace():
                return False
        elif type(widget) == Frame:
            if not EntriesNotEmpty(widget):
                return False
    return True


def NumbersOnly(value, event, string=None, max_number=None):
    """Function will return True if value is a digit"""
    if event == '1':
        for v in value:
            if not v.isdigit():
                return False
        if max_number is not None and string is not None:
            return number_limit(string, max_number)
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
        regex = re.compile('[@_!#$%^&*()<>?/|}{~:\'£=+"]')
        if regex.match(value):
            return False
        if not char_limit(string, 100):
            return False
    return True


def number_and_letters(value, string, event):
    if event == '1':
        for char in value:
            if not char.isdigit() and not char.isalpha() and not char.isspace():
                return False
        if not char_limit(string, 100):
            return False
    return True


def ValidatePhoneNumber(value, string, event):
    if event == '1':
        regex = re.compile('[+]')
        for char in value:
            if not char.isdigit() and not regex.match(char):
                return False
        if not char_limit(string, 50):
            return False
    return True


def char_limit(value, limit):
    print(value)
    print(len(value))
    if int(len(value)) >= int(limit):
        dialogs.limit_reached(limit)
        return False
    return True


def number_limit(value, limit):
    print('value: {}'.format(value))
    print('limit {}'.format(limit))
    if int(value) > int(limit):
        dialogs.number_limit_reached(limit)
        return False
    return True
