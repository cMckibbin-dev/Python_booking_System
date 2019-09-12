from tkinter import *
import ttkcalendar
from classes import *
from gui import view_details as vD


def date_top_level(event, entry):
    """function to call calender widget and insert selected value into entry box"""
    top = Toplevel()
    top.title('Selected Date')
    # calender widget
    calendar = ttkcalendar.Calendar(top)
    top.grab_set()
    top.wait_window()
    print(calendar.getselection())
    entry.delete(0, 'end')
    entry.insert(0, calendar.getselection())
    top.destroy()


def _view_details(event):
    """function to return the correct view details class for the instance of the event"""
    if isinstance(event, Conference):
        return vD.ViewDetailsConference
    elif isinstance(event, Wedding):
        return vD.ViewDetailsWedding
    elif isinstance(event, Party):
        return vD.ViewDetailsParty


def view_details_popup(event):
    """function creates a top level pop up for the view details form of a event"""
    top = Toplevel()
    top.title('View Details')
    form = _view_details(event)
    form(top, event)
    top.grab_set()
    top.wait_window()
    top.destroy()