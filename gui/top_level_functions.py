from tkinter import *
import ttkcalendar
from classes import *
from gui import view_details as vD


def date_top_level(event, master, entry):
    """function to call calender widget and insert selected value into entry box"""
    top = Toplevel()
    top.title('Selected Date')
    # calender widget
    calendar = ttkcalendar.Calendar(top)
    # master releasing control of program
    master.grab_release()
    top.grab_set()
    top.wait_window()
    print(calendar.getselection())
    entry.configure(state='normal')
    entry.delete(0, 'end')
    entry.insert(0, calendar.getselection())
    entry.configure(state='readonly')
    top.grab_release()
    master.grab_set()
    top.destroy()


def _view_details(event):
    """function to return the correct view details class for the instance of the event"""
    if isinstance(event, Conference):
        return vD.ViewDetailsConference
    elif isinstance(event, Wedding):
        return vD.ViewDetailsWedding
    elif isinstance(event, Party):
        return vD.ViewDetailsParty


def _update_form(event):
    """function returns correct update UI class for given event"""
    if isinstance(event, Conference):
        return vD.update.UpdateConferenceUI
    elif isinstance(event, Wedding):
        return vD.update.UpdateWeddingUI
    elif isinstance(event, Party):
        return vD.update.UpdatePartyUI
    else:
        print('error')


def view_details_popup(booking, parent):
    """function creates a top level pop up for the view details form of a event"""
    top = Toplevel()
    top.title('View Details')
    form = _view_details(booking)
    form(top, booking)
    top.grab_set()
    top.focus_force()
    top.wait_window()
    top.destroy()
    parent.focus_force()


def update_popup(parent, booking):
    top = Toplevel()
    top.title('Update Booking')
    form = _update_form(booking)
    form(top, booking)
    top.grab_set()
    top.focus_force()
    top.wait_window()
    top.destroy()
    parent.focus_force()
