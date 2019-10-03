"""module contains the functions used to validate user input in the update and create forms"""
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


def NumbersOnly(value, event, string=None, max_number=None, parent=None):
    """Function will return True if value is a digit and if number limit has not been reached"""
    if event == '1':
        for v in value:
            if not v.isdigit():
                return False
        if max_number is not None and string is not None:
            return number_limit(string, max_number, parent)
    return True


def lettersOnly(char, string, event, parent=None):
    """function will return true if value is a letter and character limit has not been reached"""
    if event == '1':
        for c in char:
            if not c.isalpha() and not c.isspace():
                return False
        if not char_limit(string, 100, parent):
            return False
    return True


def noSpecialCharacter(value, string, event, parent=None):
    """function returns true if value is not a special character and character limit has not been reached"""
    if event == '1':
        regex = re.compile('[@_!#$%^&*()<>?/|}{~:\'£=+"]')
        if regex.match(value):
            return False
        if not char_limit(string, 100, parent):
            return False
    return True


def number_and_letters(value, string, event, limit=None, parent=None):
    """function returns true if value is a number or letter and character limit has not been reached"""
    if event == '1':
        for char in value:
            if not char.isdigit() and not char.isalpha() and not char.isspace():
                return False

        if limit:
            if not char_limit(string, limit, parent):
                return False
    return True


def ValidatePhoneNumber(value, string, event, parent=None):
    """function returns True if value entered is a number or a + and if the character limit has not been reached"""
    if event == '1':
        regex = re.compile('[+]')
        for char in value:
            if not char.isdigit() and not regex.match(char):
                return False
        if not char_limit(string, 50, parent):
            return False
    return True


def char_limit(value, limit, parent=None):
    """function returns False if character limit has been reached or exceeded"""
    if int(len(value)) >= int(limit):
        dialogs.limit_reached(limit, parent)
        return False
    return True


def number_limit(value, limit, parent=None):
    """function returns False if number limit has been exceeded"""
    if int(value) > int(limit):
        dialogs.number_limit_reached(limit, parent)
        return False
    return True


def check_address(value, string, event, parent=None):
    """function to ensure that value entered is either a letter, number or a comma.
    Returns False if character limit has been reached"""
    
    if event == '1':
        regex = re.compile('^[a-zA-Z0-9,]')
        for char in value:
            if not regex.match(char) and not char.isspace():
                return False

        if not char_limit(string, 100, parent):
            return False
    return True
